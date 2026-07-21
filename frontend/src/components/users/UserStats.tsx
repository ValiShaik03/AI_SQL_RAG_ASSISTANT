import { Users, ShieldCheck, UserCheck, UserX } from "lucide-react";
import { Card } from "@/components/ui-kit/Card";

interface Props {
  total: number;
  active: number;
  inactive: number;
  admins: number;
}

export function UserStats({
  total,
  active,
  inactive,
  admins,
}: Props) {
  const cards = [
    {
      title: "Total Users",
      value: total,
      icon: Users,
    },
    {
      title: "Administrators",
      value: admins,
      icon: ShieldCheck,
    },
    {
      title: "Active Users",
      value: active,
      icon: UserCheck,
    },
    {
      title: "Inactive Users",
      value: inactive,
      icon: UserX,
    },
  ];

  return (
    <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <Card
          key={card.title}
          className="p-5 flex items-center justify-between"
        >
          <div>
            <p className="text-sm text-muted-foreground">
              {card.title}
            </p>

            <h2 className="text-3xl font-bold mt-2">
              {card.value}
            </h2>
          </div>

          <card.icon className="h-9 w-9 text-primary" />
        </Card>
      ))}
    </div>
  );
}