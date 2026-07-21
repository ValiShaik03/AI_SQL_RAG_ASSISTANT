import { createFileRoute } from "@tanstack/react-router";
import { Card } from "@/components/ui-kit/Card";
import { useAuth } from "@/lib/auth-context";
import { userDisplayName, userInitials } from "@/lib/auth";

export const Route = createFileRoute("/profile")({
  component: Profile,
});

function Profile() {
  const { user, role } = useAuth();
  const name = userDisplayName(user);
  const initials = userInitials(user);

  return (
    <div className="space-y-6 max-w-2xl">
      <div>
        <h1 className="text-2xl font-semibold">Profile</h1>
        <p className="text-sm text-muted-foreground">
          Your account details and session information.
        </p>
      </div>

      <Card className="flex items-center gap-4">
        <div className="h-16 w-16 rounded-full gradient-brand grid place-items-center text-white text-xl font-semibold">
          {initials}
        </div>

        <div className="min-w-0">
          <div className="font-semibold truncate">{name}</div>

          {user?.email && (
            <div className="text-sm text-muted-foreground truncate">
              {user.email as string}
            </div>
          )}

          {role && (
            <div className="mt-1 inline-flex items-center rounded-full bg-muted px-2 py-0.5 text-xs uppercase tracking-wider text-muted-foreground">
              {role}
            </div>
          )}
        </div>
      </Card>
    </div>
  );
}
