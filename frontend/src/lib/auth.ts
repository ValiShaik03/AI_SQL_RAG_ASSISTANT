// Auth utilities — JWT + user session stored in localStorage.
// Never log or expose the token.

const TOKEN_KEY = "token";
const USER_KEY = "user";

export interface AuthUser {
  id?: number | string;
  name?: string;
  full_name?: string;
  email?: string;
  role?: string;
  [k: string]: unknown;
}

export function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string) {
  localStorage.setItem(TOKEN_KEY, token);
  notifyAuthChanged();
}

export function getUser(): AuthUser | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem(USER_KEY);
    return raw ? (JSON.parse(raw) as AuthUser) : null;
  } catch {
    return null;
  }
}

export function setUser(user: AuthUser) {
  localStorage.setItem(USER_KEY, JSON.stringify(user));
  notifyAuthChanged();
}

// export function clearAuth() {
//   localStorage.removeItem(TOKEN_KEY);
//   localStorage.removeItem(USER_KEY);
//   notifyAuthChanged();
// }

export function clearAuth() {
  console.trace("clearAuth() called");

  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
  notifyAuthChanged();
}

function notifyAuthChanged() {
  if (typeof window !== "undefined") {
    window.dispatchEvent(new Event("auth:changed"));
  }
}

export function isAuthenticated(): boolean {
  return !!getToken();
}

export function userDisplayName(u: AuthUser | null): string {
  if (!u) return "User";
  return (
    (u.full_name as string) ||
    (u.name as string) ||
    (u.email as string) ||
    "User"
  );
}

export function userInitials(u: AuthUser | null): string {
  const name = userDisplayName(u);
  const parts = name.split(/[\s@]+/).filter(Boolean);
  const letters = (parts[0]?.[0] ?? "") + (parts[1]?.[0] ?? "");
  return letters.toUpperCase() || "U";
}
