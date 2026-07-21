// Auth context — thin React wrapper over the existing localStorage-based auth
// helpers in `./auth`. Keeps the current storage contract intact (token/user
// keys) while giving components a reactive way to read session state and
// perform login/logout without prop drilling.

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import {
  clearAuth,
  getToken,
  getUser,
  setToken,
  setUser,
  type AuthUser,
} from "./auth";

interface AuthContextValue {
  user: AuthUser | null;
  token: string | null;
  isAuthenticated: boolean;
  role: string | null;
  hasRole: (role: string | string[]) => boolean;
  login: (token: string, user: AuthUser) => void;
  logout: () => void;
  refresh: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setTokenState] = useState<string | null>(() => getToken());
  const [user, setUserState] = useState<AuthUser | null>(() => getUser());

  // Sync across tabs and after `clearAuth()` calls from the axios interceptor.
  useEffect(() => {
    const sync = () => {
      setTokenState(getToken());
      setUserState(getUser());
    };
    window.addEventListener("storage", sync);
    window.addEventListener("auth:changed", sync);
    return () => {
      window.removeEventListener("storage", sync);
      window.removeEventListener("auth:changed", sync);
    };
  }, []);

  const login = useCallback((nextToken: string, nextUser: AuthUser) => {
    setToken(nextToken);
    setUser(nextUser);
    setTokenState(nextToken);
    setUserState(nextUser);
    window.dispatchEvent(new Event("auth:changed"));
  }, []);

  const logout = useCallback(() => {
    clearAuth();
    setTokenState(null);
    setUserState(null);
    window.dispatchEvent(new Event("auth:changed"));
  }, []);

  const refresh = useCallback(() => {
    setTokenState(getToken());
    setUserState(getUser());
  }, []);

  const role = (user?.role as string | undefined) ?? null;

  const hasRole = useCallback(
    (roleOrRoles: string | string[]) => {
      if (!role) return false;
      const list = Array.isArray(roleOrRoles) ? roleOrRoles : [roleOrRoles];
      return list.map((r) => r.toLowerCase()).includes(role.toLowerCase());
    },
    [role],
  );

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      token,
      isAuthenticated: !!token,
      role,
      hasRole,
      login,
      logout,
      refresh,
    }),
    [user, token, role, hasRole, login, logout, refresh],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within <AuthProvider>");
  return ctx;
}
