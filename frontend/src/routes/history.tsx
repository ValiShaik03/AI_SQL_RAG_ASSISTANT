
import { createFileRoute } from "@tanstack/react-router";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { Card } from "@/components/ui-kit/Card";
import { Loader } from "@/components/ui-kit/Loader";
import { EmptyState, ErrorState } from "@/components/ui-kit/States";
import { DataTable } from "@/components/ui-kit/DataTable";
import { Button } from "@/components/ui-kit/Button";
import { History, Trash2 } from "lucide-react";
import { services } from "@/api/services";

export const Route = createFileRoute("/history")({
  component: QueryHistory,
});

export default function QueryHistory() {
  const qc = useQueryClient();

  const history = useQuery({
    queryKey: ["history"],
    queryFn: services.history,
  });

  const del = useMutation({
    mutationFn: (id: number) => services.deleteHistory(id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["history"] }),
  });

  if (history.isLoading) return <Loader />;
  if (history.isError)
    return (
      <ErrorState
        title="Failed to load history"
        description="Please try again."
      />
    );

  const rows = Array.isArray(history.data)
    ? history.data
    : history.data?.history ?? history.data?.items ?? [];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">Query History</h1>
        <p className="text-sm text-muted-foreground">
          Review previous AI SQL questions and generated SQL.
        </p>
      </div>

      <Card>
        {rows.length === 0 ? (
          <EmptyState
            icon={<History className="h-6 w-6" />}
            title="No query history"
            description="Your previous AI SQL conversations will appear here."
          />
        ) : (
          <DataTable
            data={rows}
            columns={[
              { key: "question", label: "Question" },
              { key: "generated_sql", label: "Generated SQL" },
              { key: "answer", label: "Answer" },
              { key: "created_at", label: "Created" },
              {
                key: "id",
                label: "Action",
                sortable: false,
                render: (row: any) => (
                  <Button
                    size="sm"
                    variant="destructive"
                    onClick={() => del.mutate(row.id)}
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                ),
              },
            ]}
          />
        )}
      </Card>
    </div>
  );
}
