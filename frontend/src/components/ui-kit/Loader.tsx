import { cn } from "@/lib/utils";

export function Skeleton({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "animate-pulse rounded-lg bg-muted/60",
        className,
      )}
    />
  );
}

export function Loader({ label }: { label?: string }) {
  return (
    <div className="flex items-center gap-3 text-muted-foreground text-sm">
      <div className="h-4 w-4 rounded-full border-2 border-primary border-t-transparent animate-spin" />
      {label ?? "Loading..."}
    </div>
  );
}
