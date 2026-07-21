import { createFileRoute } from "@tanstack/react-router";
import { useQueries } from "@tanstack/react-query";
import { useMemo } from "react";
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  LineChart,
  Line,
} from "recharts";
import { services } from "@/api/services";
import { ChartCard } from "@/components/ui-kit/ChartCard";
import { Card } from "@/components/ui-kit/Card";
import { StatCard } from "@/components/ui-kit/StatCard";
import { ErrorState } from "@/components/ui-kit/States";
import { Loader } from "@/components/ui-kit/Loader";
import { Lightbulb } from "lucide-react";

export const Route = createFileRoute("/analytics")({
  component: AnalyticsPage,
});

const COLORS = ["#a78bfa", "#60a5fa", "#f472b6", "#34d399", "#fbbf24", "#f87171", "#22d3ee"];

const tooltipContentStyle: React.CSSProperties = {
  backgroundColor: "#111827",
  border: "1px solid rgba(255,255,255,0.08)",
  borderRadius: "8px",
  padding: "14px 16px",
  boxShadow: "0 10px 30px rgba(0,0,0,0.45)",
  color: "#FFFFFF",
  opacity: 1,
  fontSize: "14px",
  lineHeight: 1.4,
};
const tooltipItemStyle: React.CSSProperties = {
  color: "#60A5FA",
  fontSize: "14px",
  fontWeight: 600,
};
const tooltipLabelStyle: React.CSSProperties = {
  color: "#FFFFFF",
  fontSize: "14px",
  fontWeight: 600,
  marginBottom: "4px",
};
const tooltipCursor = { fill: "rgba(167,139,250,0.12)" };
const tooltipWrapperStyle: React.CSSProperties = { outline: "none", zIndex: 50 };

function bucketSalaries(items: any[]): { name: string; value: number }[] {
  if (!items?.length) return [];
  const values = items
    .map((d) => Number(d.salary ?? d.value ?? d))
    .filter((n) => Number.isFinite(n));
  if (!values.length) return [];
  const min = Math.min(...values);
  const max = Math.max(...values);
  const step = Math.max(1, Math.ceil((max - min + 1) / 5));
  const buckets: Record<string, number> = {};
  for (const v of values) {
    const start = Math.floor((v - min) / step) * step + min;
    const end = start + step - 1;
    const label = `$${(start / 1000).toFixed(0)}k-${(end / 1000).toFixed(0)}k`;
    buckets[label] = (buckets[label] ?? 0) + 1;
  }
  return Object.entries(buckets).map(([name, value]) => ({ name, value }));
}

function money(v: unknown) {
  if (v == null || Number.isNaN(Number(v))) return "—";
  return `$${Number(v).toLocaleString(undefined, { maximumFractionDigits: 0 })}`;
}

function AnalyticsPage() {
  const q = useQueries({
    queries: [
      { queryKey: ["a-depts"], queryFn: services.analyticsDepartments, retry: 0, staleTime: 60_000 },
      { queryKey: ["a-salary"], queryFn: services.analyticsSalary, retry: 0, staleTime: 60_000 },
      { queryKey: ["a-hiring"], queryFn: services.analyticsHiring, retry: 0, staleTime: 60_000 },
      { queryKey: ["a-dashboard"], queryFn: services.dashboard, retry: 0, staleTime: 60_000 },
      { queryKey: ["a-insights"], queryFn: services.insights, retry: 0, staleTime: 60_000 },
    ],
  });

  const [depts, salary, hiring, dashboard, insights] = q;

  const depData = useMemo(
    () =>
      (Array.isArray(depts.data) ? depts.data : []).map((d: any) => ({
        name: d.department ?? d.name ?? "—",
        value: Number(d.total ?? d.count ?? d.value ?? 0),
      })),
    [depts.data],
  );

  const salaryData = useMemo(
    () => bucketSalaries(Array.isArray(salary.data) ? salary.data : []),
    [salary.data],
  );

  const hiringData = useMemo(
    () =>
      (Array.isArray(hiring.data) ? hiring.data : []).map((d: any) => ({
        name: String(d.year ?? d.period ?? d.month ?? d.name ?? "—"),
        value: Number(d.total ?? d.hires ?? d.count ?? d.value ?? 0),
      })),
    [hiring.data],
  );

  const dashboardData: any = dashboard.data ?? {};

  const dash = dashboardData.metrics ?? {};
  const ins = dashboardData.insights ?? insights.data ?? {};

  const metrics = [
    { label: "Total Employees", value: ins.total_employees ?? dash.employees },
    { label: "Departments", value: dash.departments },
    { label: "Average Salary", value: money(ins.average_salary ?? dash.avg_salary) },
    { label: "Max Salary", value: money(dash.max_salary) },
  ];

  const anyError = q.some((x) => x.isError);

  return (
    <div className="max-w-7xl mx-auto flex flex-col gap-6">
      <div>
        <div className="text-xs uppercase tracking-widest text-muted-foreground">Analytics</div>
        <h1 className="text-3xl font-bold gradient-text mt-1">Insights & Trends</h1>
      </div>

      {anyError && (
        <ErrorState
          title="Some analytics endpoints failed"
          description="Available data still renders below."
        />
      )}

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {metrics.map((m) => (
          <StatCard
            key={m.label}
            label={m.label}
            value={
              m.value == null || m.value === "—"
                ? "—"
                : typeof m.value === "number"
                ? m.value.toLocaleString()
                : String(m.value)
            }
            loading={dashboard.isLoading || insights.isLoading}
          />
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ChartCard title="Department Distribution" description="Employees per department">
          {depts.isLoading ? (
            <Loader />
          ) : depData.length === 0 ? (
            <div className="grid h-full place-items-center text-sm text-muted-foreground">No data</div>
          ) : (
            <ResponsiveContainer>
              <PieChart>
                <Pie data={depData} dataKey="value" nameKey="name" outerRadius={100} innerRadius={50}>
                  {depData.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={tooltipContentStyle}
                  itemStyle={tooltipItemStyle}
                  labelStyle={tooltipLabelStyle}
                  wrapperStyle={tooltipWrapperStyle}
                  cursor={tooltipCursor}
                />
              </PieChart>
            </ResponsiveContainer>
          )}
        </ChartCard>

        <ChartCard title="Salary Distribution" description="Count by salary bucket">
          {salary.isLoading ? (
            <Loader />
          ) : salaryData.length === 0 ? (
            <div className="grid h-full place-items-center text-sm text-muted-foreground">No data</div>
          ) : (
            <ResponsiveContainer>
              <BarChart data={salaryData}>
                <defs>
                  <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#a78bfa" />
                    <stop offset="100%" stopColor="#60a5fa" />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
                <XAxis dataKey="name" stroke="var(--muted-foreground)" fontSize={11} />
                <YAxis stroke="var(--muted-foreground)" fontSize={11} allowDecimals={false} />
                <Tooltip
                  contentStyle={tooltipContentStyle}
                  itemStyle={tooltipItemStyle}
                  labelStyle={tooltipLabelStyle}
                  wrapperStyle={tooltipWrapperStyle}
                  cursor={tooltipCursor}
                />
                <Bar dataKey="value" fill="url(#g1)" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          )}
        </ChartCard>

        <ChartCard title="Hiring Trend" description="New hires over time" className="lg:col-span-2">
          {hiring.isLoading ? (
            <Loader />
          ) : hiringData.length === 0 ? (
            <div className="grid h-full place-items-center text-sm text-muted-foreground">No data</div>
          ) : (
            <ResponsiveContainer>
              <LineChart data={hiringData}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
                <XAxis dataKey="name" stroke="var(--muted-foreground)" fontSize={11} />
                <YAxis stroke="var(--muted-foreground)" fontSize={11} allowDecimals={false} />
                <Tooltip
                  contentStyle={tooltipContentStyle}
                  itemStyle={tooltipItemStyle}
                  labelStyle={tooltipLabelStyle}
                  wrapperStyle={tooltipWrapperStyle}
                  cursor={tooltipCursor}
                />
                <Line type="monotone" dataKey="value" stroke="#a78bfa" strokeWidth={3} dot={{ r: 4 }} />
              </LineChart>
            </ResponsiveContainer>
          )}
        </ChartCard>
      </div>

      <Card>
        <div className="flex items-center gap-2 mb-3">
          <Lightbulb className="h-4 w-4 text-primary" />
          <h3 className="font-semibold">Insights</h3>
        </div>
        {insights.isLoading ? (
          <Loader />
        ) : insights.data ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm">
            {ins.highest_paid_department && (
              <div className="rounded-xl bg-muted/40 p-4">
                <div className="text-xs text-muted-foreground">Highest Paid Department</div>
                <div className="font-medium mt-1">
                  {ins.highest_paid_department.department} · {money(ins.highest_paid_department.avg_salary)}
                </div>
              </div>
            )}
            {ins.lowest_paid_department && (
              <div className="rounded-xl bg-muted/40 p-4">
                <div className="text-xs text-muted-foreground">Lowest Paid Department</div>
                <div className="font-medium mt-1">
                  {ins.lowest_paid_department.department} · {money(ins.lowest_paid_department.avg_salary)}
                </div>
              </div>
            )}
            {ins.latest_hiring_year != null && (
              <div className="rounded-xl bg-muted/40 p-4">
                <div className="text-xs text-muted-foreground">Latest Hiring Year</div>
                <div className="font-medium mt-1">{ins.latest_hiring_year}</div>
              </div>
            )}
            {ins.total_employees != null && (
              <div className="rounded-xl bg-muted/40 p-4">
                <div className="text-xs text-muted-foreground">Total Employees</div>
                <div className="font-medium mt-1">{ins.total_employees}</div>
              </div>
            )}
          </div>
        ) : (
          <p className="text-sm text-muted-foreground">No insights available.</p>
        )}
      </Card>
    </div>
  );
}
