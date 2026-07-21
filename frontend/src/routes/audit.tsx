
import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import { Card } from "@/components/ui-kit/Card";
import { Loader } from "@/components/ui-kit/Loader";
import { EmptyState, ErrorState } from "@/components/ui-kit/States";
import { DataTable } from "@/components/ui-kit/DataTable";
import { ProtectedRoute } from "@/components/auth/ProtectedRoute";
import { ShieldCheck } from "lucide-react";
import { services } from "@/api/services";

export const Route = createFileRoute("/audit")({
  component: () => (
    <ProtectedRoute roles={["admin","administrator"]}>
      <AuditLogs />
    </ProtectedRoute>
  ),
});

function AuditLogs() {
  const audit = useQuery({
    queryKey:["audit-logs"],
    queryFn:()=>services.auditLogs(1,100),
  });

  if(audit.isLoading) return <Loader />;
  if(audit.isError){
    return <ErrorState title="Failed to load audit logs" description="Please try again."/>;
  }

  const rows = Array.isArray(audit.data)
    ? audit.data
    : audit.data?.logs ?? audit.data?.items ?? audit.data?.data ?? [];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">Audit Logs</h1>
        <p className="text-sm text-muted-foreground">
          Track privileged actions across the workspace.
        </p>
      </div>

      <Card>
        {rows.length===0 ? (
          <EmptyState
            icon={<ShieldCheck className="h-6 w-6"/>}
            title="No audit events"
            description="No audit records are available."
          />
        ) : (
          <DataTable
            data={rows}
            columns={[
              {key:"timestamp",label:"Timestamp"},
              {key:"user_id",label:"User"},
              {key:"action",label:"Action"},
              {key:"resource",label:"Resource"},
              {key:"status",label:"Status"},
            ]}
          />
        )}
      </Card>
    </div>
  );
}
