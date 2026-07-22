import axios, { AxiosError } from "axios";
import { getBaseUrl } from "@/lib/config";
import { clearAuth, getToken } from "@/lib/auth";

export const api = axios.create({
  timeout: 60_000,
});

api.interceptors.request.use((config) => {
  config.baseURL = getBaseUrl();
  const token = getToken();
  if (token) {
    config.headers = config.headers ?? {};
    (config.headers as Record<string, string>).Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle expired/invalid sessions globally.
// api.interceptors.response.use(
//   (r) => r,
//   (error: AxiosError) => {
//     const status = error.response?.status;
//     if (status === 401 || status === 403) {
//       const onLogin =
//         typeof window !== "undefined" &&
//         window.location.pathname.startsWith("/login");
//       if (!onLogin) {
//         clearAuth();
//         if (typeof window !== "undefined") {
//           const msg = encodeURIComponent("Session expired. Please login again.");
//           window.location.replace(`/login?reason=${msg}`);
//         }
//       }
//     }
//     return Promise.reject(error);
//   },
// );

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.log("========== AXIOS ERROR ==========");
    console.log("URL:", error.config?.url);
    console.log("Status:", error.response?.status);
    console.log("Response:", error.response?.data);

    const status = error.response?.status;

    if (status === 401) {
    clearAuth();

    const msg = encodeURIComponent(
        "Session expired. Please login again."
    );

    window.location.replace(`/login?reason=${msg}`);
}

return Promise.reject(error);
  }
);


/**
 * Extract a human-readable error message from an axios/backend error.
 * Prefers backend-provided `message` / `detail` / `error` fields, and only
 * falls back to a generic network message when there is truly no response.
 */
export function extractApiError(err: unknown, fallback = "Something went wrong"): string {
  if (axios.isAxiosError(err)) {
    const data = err.response?.data as
      | { message?: string; detail?: string; error?: string }
      | undefined;
    if (data) {
      const msg = data.message || data.detail || data.error;
      if (msg && typeof msg === "string") return msg;
    }
    if (!err.response) return "Unable to reach the backend. Please check your connection.";
  }
  if (err instanceof Error && err.message) return err.message;
  return fallback;
}
