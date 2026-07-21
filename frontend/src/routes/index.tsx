import { createFileRoute } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import {
  Activity,
  Database,
  Users,
  Building2,
  DollarSign,
  TrendingUp,
  FolderKanban,
  Table2,
  Rows3,
  ServerCog,
} from "lucide-react";
import { services } from "@/api/services";
import { StatCard } from "@/components/ui-kit/StatCard";
import { Card } from "@/components/ui-kit/Card";
import { ErrorState } from "@/components/ui-kit/States";
import { Button } from "@/components/ui-kit/Button";

export const Route = createFileRoute("/")({
  component: DashboardPage,
});

function fmt(v: unknown, fallback = "—") {
  if (v == null || v === "") return fallback;
  if (typeof v === "number") return v.toLocaleString();
  return String(v);
}

function money(v: unknown) {
  if (v == null || Number.isNaN(Number(v))) return "—";
  return `$${Number(v).toLocaleString(undefined, { maximumFractionDigits: 0 })}`;
}

function titleCase(s: string) {
  return s
    .replace(/[_-]+/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function DashboardPage() {
  const [healthQ, dashQ, insightsQ, statsQ] = useQueries({
    queries: [
      { queryKey: ["health"], queryFn: services.health, refetchInterval: 30_000, retry: 1 },
      { queryKey: ["dashboard"], queryFn: services.dashboard, retry: 1, staleTime: 60_000 },
      { queryKey: ["insights"], queryFn: services.insights, retry: 1, staleTime: 60_000 },
      { queryKey: ["dbStats"], queryFn: services.dbStats, retry: 1, staleTime: 60_000 },
    ],
  });

  const health: any = healthQ.data ?? {};
  const dashboard = dashQ.data ?? {};
  const dash = dashboard.metrics ?? {};
  const insights = dashboard.insights ?? {};
  const stats = statsQ.data ?? {};

  const totalEmployees = insights.total_employees ?? dash.employees;
  const totalDepartments = dash.departments;
  const avgSalary = insights.average_salary ?? dash.avg_salary;
  const maxSalary = dash.max_salary;
  const tables: Array<{ table: string; rows: number; columns: number }> = Array.isArray(
    stats.tables,
  )
    ? stats.tables
    : [];
  const projectsCount = tables.find((t) => t.table === "projects")?.rows;
  const totalTables = stats.total_tables ?? tables.length;
  const totalRows =
    stats.total_rows ??
    (tables.length ? tables.reduce((s, t) => s + (Number(t.rows) || 0), 0) : undefined);
  const totalColumns =
    stats.total_columns ??
    (tables.length ? tables.reduce((s, t) => s + (Number(t.columns) || 0), 0) : undefined);
  const dbName = stats.database ?? "MySQL";

  const allError = healthQ.isError && dashQ.isError && insightsQ.isError;
  const anyFetching =
    healthQ.isFetching || dashQ.isFetching || insightsQ.isFetching || statsQ.isFetching;

  const apiHealthy = health.status === "healthy";
  const dbHealthy = String(health.database ?? "").toLowerCase() === "connected";

  const refetchAll = () => {
    healthQ.refetch();
    dashQ.refetch();
    insightsQ.refetch();
    statsQ.refetch();
  };

  return (
    <div className="max-w-7xl mx-auto flex flex-col gap-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <div className="text-xs uppercase tracking-widest text-muted-foreground">
            Overview
          </div>
          <h1 className="text-3xl font-bold gradient-text mt-1">Dashboard</h1>
          <p className="text-muted-foreground text-sm mt-1">
            Real-time status of your AI SQL RAG backend.
          </p>
        </div>
        <Button
            variant="ghost"
            onClick={refetchAll}
            disabled={anyFetching}
        >
            {anyFetching ? "Refreshing..." : "🔄 Refresh"}
        </Button>
</div>
      {allError ? (
        <ErrorState
          title="Could not reach backend"
          description="Check the base URL in Settings or verify your Render deployment is awake."
          onRetry={refetchAll}
        />
      ) : (
        <>
          {/* KPI grid */}
          <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
            <StatCard
              label="Backend Status"
              icon={<Activity className="h-4 w-4" />}
              loading={healthQ.isLoading}
              value={
                <span className="inline-flex items-center gap-2">
                  <span
                    className={`h-2.5 w-2.5 rounded-full ${
                      apiHealthy
                        ? "bg-[color:var(--success)] animate-pulse"
                        : "bg-destructive"
                    }`}
                  />
                  {fmt(health.status ?? (healthQ.isError ? "Offline" : "Unknown"))}
                </span>
              }
            />
            <StatCard
              label="Database Status"
              icon={<Database className="h-4 w-4" />}
              loading={healthQ.isLoading}
              value={
                <span className="inline-flex items-center gap-2">
                  <span
                    className={`h-2.5 w-2.5 rounded-full ${
                      dbHealthy ? "bg-[color:var(--success)]" : "bg-destructive"
                    }`}
                  />
                  {fmt(health.database ?? (healthQ.isError ? "Unavailable" : "—"))}
                </span>
              }
            />
            <StatCard
              label="Employees"
              icon={<Users className="h-4 w-4" />}
              loading={dashQ.isLoading || insightsQ.isLoading}
              value={fmt(totalEmployees)}
            />
            <StatCard
              label="Departments"
              icon={<Building2 className="h-4 w-4" />}
              loading={dashQ.isLoading}
              value={fmt(totalDepartments)}
            />
            <StatCard
              label="Projects"
              icon={<FolderKanban className="h-4 w-4" />}
              loading={statsQ.isLoading}
              value={fmt(projectsCount)}
            />
            <StatCard
              label="Average Salary"
              icon={<DollarSign className="h-4 w-4" />}
              loading={dashQ.isLoading || insightsQ.isLoading}
              value={money(avgSalary)}
            />
            <StatCard
              label="Highest Salary"
              icon={<TrendingUp className="h-4 w-4" />}
              loading={dashQ.isLoading}
              value={money(maxSalary)}
            />
            <StatCard
              label="Database Tables"
              icon={<Table2 className="h-4 w-4" />}
              loading={statsQ.isLoading}
              value={fmt(totalTables)}
            />
            <StatCard
              label="Database Rows"
              icon={<Rows3 className="h-4 w-4" />}
              loading={statsQ.isLoading}
              value={fmt(totalRows)}
            />
          </div>

          {/* Database overview */}
          <Card className="flex flex-col gap-5">
            <div className="flex items-start justify-between gap-4 flex-wrap">
              <div className="flex items-center gap-3">
                <div className="h-11 w-11 rounded-xl gradient-brand grid place-items-center shadow-lg shadow-primary/30">
                  <ServerCog className="h-5 w-5 text-white" />
                </div>
                <div>
                  <h3 className="font-semibold">Database Overview</h3>
                  <p className="text-xs text-muted-foreground mt-0.5">
                    Live schema snapshot from your backend.
                  </p>
                </div>
              </div>
              <div className="grid grid-cols-4 gap-2 text-center">
                <MiniStat label="Database" value={String(dbName).toUpperCase()} />
                <MiniStat label="Tables" value={fmt(totalTables)} />
                <MiniStat label="Rows" value={fmt(totalRows)} />
                <MiniStat label="Columns" value={fmt(totalColumns)} />
              </div>
            </div>

            {statsQ.isLoading ? (
              <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3">
                {Array.from({ length: 8 }).map((_, i) => (
                  <div key={i} className="h-24 rounded-xl bg-muted/40 animate-pulse" />
                ))}
              </div>
            ) : tables.length === 0 ? (
              <div className="text-sm text-muted-foreground py-6 text-center">
                No table statistics available.
              </div>
            ) : (
              <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3">
                {tables.map((t) => (
                  <div
                    key={t.table}
                    className="rounded-xl border border-border bg-muted/40 p-4 flex flex-col gap-1 hover:border-primary/50 hover:bg-muted/60 hover:-translate-y-0.5 transition-all"
                  >
                    <div className="flex items-center gap-2 text-xs text-muted-foreground">
                      <Table2 className="h-3.5 w-3.5" />
                      <span className="uppercase tracking-wider text-[10px]">Table</span>
                    </div>
                    <div className="font-semibold text-sm truncate" title={t.table}>
                      {titleCase(t.table)}
                    </div>
                    <div className="flex items-center gap-3 mt-1 text-xs text-muted-foreground">
                      <span className="inline-flex items-center gap-1">
                        <Rows3 className="h-3 w-3" />
                        {Number(t.rows ?? 0).toLocaleString()} rows
                      </span>
                      <span>·</span>
                      <span>{Number(t.columns ?? 0).toLocaleString()} cols</span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </Card>
        </>
      )}
    </div>
  );
}

function MiniStat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-lg bg-muted/40 border border-border px-3 py-2 min-w-[80px]">
      <div className="text-[10px] uppercase tracking-wider text-muted-foreground">
        {label}
      </div>
      <div className="text-sm font-semibold truncate">{value}</div>
    </div>
  );
}
