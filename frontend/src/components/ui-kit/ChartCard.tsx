import type { ReactNode } from "react";
import { Card } from "./Card";

interface Props {
  title: string;
  description?: string;
  right?: ReactNode;
  children: ReactNode;
  className?: string;
}

export function ChartCard({ title, description, right, children, className }: Props) {
  return (
    <Card className={className}>
      <div className="mb-4 flex items-start justify-between gap-4">
        <div>
          <h3 className="font-semibold">{title}</h3>
          {description && (
            <p className="text-xs text-muted-foreground mt-0.5">{description}</p>
          )}
        </div>
        {right}
      </div>
      <div className="h-72 w-full">{children}</div>
    </Card>
  );
}
