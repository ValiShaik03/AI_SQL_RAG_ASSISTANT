import type { ReactNode } from "react";
import { Card } from "./Card";
import { Inbox, AlertTriangle } from "lucide-react";

export function EmptyState({
  title = "Nothing here yet",
  description,
  icon,
  action,
}: {
  title?: string;
  description?: string;
  icon?: ReactNode;
  action?: ReactNode;
}) {
  return (
    <Card className="flex flex-col items-center text-center py-12 gap-3">
      <div className="h-12 w-12 rounded-full grid place-items-center bg-muted text-muted-foreground">
        {icon ?? <Inbox className="h-6 w-6" />}
      </div>
      <h3 className="font-semibold">{title}</h3>
      {description && (
        <p className="text-sm text-muted-foreground max-w-sm">{description}</p>
      )}
      {action}
    </Card>
  );
}

export function ErrorState({
  title = "Something went wrong",
  description,
  onRetry,
}: {
  title?: string;
  description?: string;
  onRetry?: () => void;
}) {
  return (
    <Card className="flex flex-col items-center text-center py-10 gap-3 border-destructive/40">
      <div className="h-12 w-12 rounded-full grid place-items-center bg-destructive/15 text-destructive">
        <AlertTriangle className="h-6 w-6" />
      </div>
      <h3 className="font-semibold">{title}</h3>
      {description && (
        <p className="text-sm text-muted-foreground max-w-md">{description}</p>
      )}
      {onRetry && (
        <button
          onClick={onRetry}
          className="mt-1 h-9 px-4 rounded-xl bg-destructive text-destructive-foreground text-sm hover:opacity-90"
        >
          Retry
        </button>
      )}
    </Card>
  );
}
