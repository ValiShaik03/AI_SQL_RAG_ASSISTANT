import type { ReactNode, HTMLAttributes } from "react";
import { cn } from "@/lib/utils";

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  glass?: boolean;
}

export function Card({ children, className, glass = true, ...rest }: CardProps) {
  return (
    <div
      {...rest}
      className={cn(
        "rounded-2xl p-5 shadow-lg shadow-black/5 transition",
        glass ? "glass" : "bg-card border border-border",
        className,
      )}
    >
      {children}
    </div>
  );
}
