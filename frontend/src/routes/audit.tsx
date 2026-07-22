
import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import { Card } from "@/components/ui-kit/Card";
import { Loader } from "@/components/ui-kit/Loader";
import { EmptyState, ErrorState } from "@/components/ui-kit/States";
import { ProtectedRoute } from "@/components/auth/ProtectedRoute";
import { ShieldCheck } from "lucide-react";
import { services } from "@/api/services";
import { useMemo, useState } from "react";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Search } from "lucide-react";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
export const Route = createFileRoute("/audit")({
  component: () => (
    <ProtectedRoute roles={["admin","administrator"]}>
      <AuditLogs />
    </ProtectedRoute>
  ),
});

const actionColor = (action: string) => {
  switch (action) {
    case "LOGIN":
      return "bg-green-600";

    case "CREATE_USER":
      return "bg-blue-600";

    case "UPDATE_USER":
      return "bg-purple-600";

    case "UPDATE_USER_STATUS":
      return "bg-indigo-600";

    case "DELETE_USER":
      return "bg-red-600";

    case "RESET_PASSWORD":
      return "bg-orange-600";

    default:
      return "bg-gray-600";
  }
};

function AuditLogs() {
  const audit = useQuery({
  queryKey: ["audit-logs"],
  queryFn: () => services.auditLogs(1, 100),
});

// ✅ Hooks must come immediately after other hooks
const [search, setSearch] = useState("");

const rows = Array.isArray(audit.data)
  ? audit.data
  : audit.data?.logs ?? audit.data?.items ?? audit.data?.data ?? [];

const filteredLogs = useMemo(() => {
  const value = search.toLowerCase();

  return rows.filter((log: any) =>
    log.full_name?.toLowerCase().includes(value) ||
    log.email?.toLowerCase().includes(value) ||
    log.action?.toLowerCase().includes(value) ||
    log.description?.toLowerCase().includes(value)
  );
}, [rows, search]);

// ✅ Early returns AFTER all hooks
if (audit.isLoading) {
  return <Loader />;
}

if (audit.isError) {
  return (
    <ErrorState
      title="Failed to load audit logs"
      description="Please try again."
    />
  );
}

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
          <>
  <div className="p-6 pb-0">
    <div className="relative w-80">
      <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />

      <Input
        placeholder="Search audit logs..."
        className="pl-10"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </div>
  </div>

  <Table>

    <TableHeader>

      <TableRow>

        <TableHead>Timestamp</TableHead>

        <TableHead>User</TableHead>

        <TableHead>Action</TableHead>

        <TableHead>Description</TableHead>

      </TableRow>

    </TableHeader>

    <TableBody>

  {filteredLogs.map((log: any) => (

    <TableRow key={log.log_id}>

      <TableCell>
        {new Date(log.created_at).toLocaleString("en-IN", {
          day: "2-digit",
          month: "short",
          year: "numeric",
          hour: "2-digit",
          minute: "2-digit",
        })}
      </TableCell>

      <TableCell>
        <div className="flex flex-col">
          <span className="font-medium">
            {log.full_name}
          </span>

          <span className="text-xs text-muted-foreground">
            {log.email}
          </span>
        </div>
      </TableCell>

      <TableCell>
        <Badge className={actionColor(log.action)}>
          {log.action.replaceAll("_", " ")}
        </Badge>
      </TableCell>

      <TableCell className="max-w-lg whitespace-normal">
        {log.description}
      </TableCell>

    </TableRow>

  ))}

</TableBody>
</Table>
</>
        )}
      </Card>
    </div>
  );
}
