import { useEffect, type ReactNode } from "react";
import { useNavigate, useRouterState } from "@tanstack/react-router";
import { useAuth } from "@/lib/auth-context";
import { EmptyState } from "@/components/ui-kit/States";

interface ProtectedRouteProps {
  children: ReactNode;
  /** Optional role(s) required to view the wrapped content. */
  roles?: string | string[];
}

/**
 * Reusable guard for authenticated routes.
 * - Redirects unauthenticated users to /login with `redirect` search param.
 * - When `roles` is provided, blocks users without a matching role.
 */
export function ProtectedRoute({ children, roles }: ProtectedRouteProps) {
  const { isAuthenticated, hasRole } = useAuth();
  const navigate = useNavigate();
  const pathname = useRouterState({ select: (s) => s.location.pathname });

  useEffect(() => {
    if (!isAuthenticated) {
      navigate({ to: "/login", search: { redirect: pathname } });
    }
  }, [isAuthenticated, navigate, pathname]);

  if (!isAuthenticated) return null;

  if (roles && !hasRole(roles)) {
    return (
      <EmptyState
        title="Access restricted"
        description="You don't have permission to view this page. Contact an administrator if you believe this is a mistake."
      />
    );
  }

  return <>{children}</>;
}
