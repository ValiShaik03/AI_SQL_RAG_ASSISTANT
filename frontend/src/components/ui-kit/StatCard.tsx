import type { ReactNode } from "react";
import { Card } from "./Card";

interface Props {
  label: string;
  value: ReactNode;
  icon?: ReactNode;
  hint?: ReactNode;
  loading?: boolean;
}

export function StatCard({ label, value, icon, hint, loading }: Props) {
  return (
    <Card className="flex flex-col gap-2">
      <div className="flex items-center justify-between text-muted-foreground text-xs uppercase tracking-wider">
        <span>{label}</span>
        {icon}
      </div>
      <div className="text-2xl font-semibold">
        {loading ? <span className="inline-block h-7 w-20 rounded bg-muted animate-pulse" /> : value}
      </div>
      {hint && <div className="text-xs text-muted-foreground">{hint}</div>}
    </Card>
  );
}
