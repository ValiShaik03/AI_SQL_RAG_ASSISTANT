import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import {
  services,
  type Employee,
  employeeDisplayName,
  employeeId,
  employeeHireDate,
} from "@/api/services";
import { DataTable, type Column } from "@/components/ui-kit/DataTable";
import { ErrorState } from "@/components/ui-kit/States";
import { Skeleton } from "@/components/ui-kit/Loader";
import { Card } from "@/components/ui-kit/Card";

export const Route = createFileRoute("/employees")({
  component: EmployeesPage,
});

interface NormalizedEmployee {
  id: number | string;
  name: string;
  email: string;
  department: string;
  designation: string;
  salary: number | null;
  hire_date: string;
  [k: string]: unknown;
}

function initials(name: string) {
  return (
    name
      .split(/\s+/)
      .map((s) => s[0])
      .filter(Boolean)
      .slice(0, 2)
      .join("")
      .toUpperCase() || "?"
  );
}

const DEPT_COLORS = [
  "bg-violet-500/15 text-violet-300 border-violet-500/30",
  "bg-sky-500/15 text-sky-300 border-sky-500/30",
  "bg-emerald-500/15 text-emerald-300 border-emerald-500/30",
  "bg-amber-500/15 text-amber-300 border-amber-500/30",
  "bg-pink-500/15 text-pink-300 border-pink-500/30",
  "bg-cyan-500/15 text-cyan-300 border-cyan-500/30",
  "bg-rose-500/15 text-rose-300 border-rose-500/30",
];

function deptColor(name: string) {
  let h = 0;
  for (let i = 0; i < name.length; i++) h = (h * 31 + name.charCodeAt(i)) | 0;
  return DEPT_COLORS[Math.abs(h) % DEPT_COLORS.length];
}

function salaryTier(v: number | null) {
  if (v == null) return "bg-muted/50 text-muted-foreground border-border";
  if (v >= 100_000) return "bg-emerald-500/15 text-emerald-300 border-emerald-500/30";
  if (v >= 70_000) return "bg-sky-500/15 text-sky-300 border-sky-500/30";
  if (v >= 50_000) return "bg-amber-500/15 text-amber-300 border-amber-500/30";
  return "bg-muted/60 text-muted-foreground border-border";
}

const columns: Column<NormalizedEmployee>[] = [
  { key: "id", label: "ID", className: "w-16 text-muted-foreground" },
  {
    key: "name",
    label: "Employee",
    render: (row) => (
      <div className="flex items-center gap-3 min-w-0">
        <div className="h-9 w-9 shrink-0 rounded-full gradient-brand text-white text-xs grid place-items-center font-semibold shadow-md shadow-primary/20">
          {initials(row.name)}
        </div>
        <div className="flex flex-col min-w-0">
          <span className="font-medium truncate">{row.name}</span>
          <span className="text-xs text-muted-foreground truncate">{row.email}</span>
        </div>
      </div>
    ),
  },
  {
    key: "department",
    label: "Department",
    render: (row) => (
      <span
        className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium border ${deptColor(
          row.department,
        )}`}
      >
        {row.department}
      </span>
    ),
  },
  { key: "designation", label: "Designation" },
  {
    key: "salary",
    label: "Salary",
    render: (row) => (
      <span
        className={`inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-semibold border ${salaryTier(
          row.salary,
        )}`}
      >
        {row.salary != null ? `$${Number(row.salary).toLocaleString()}` : "—"}
      </span>
    ),
  },
  { key: "hire_date", label: "Hire Date", className: "text-muted-foreground" },
];

function normalize(list: Employee[]): NormalizedEmployee[] {
  return list.map((e, i) => ({
    id: employeeId(e) ?? i + 1,
    name: employeeDisplayName(e),
    email: (e.email as string) ?? "—",
    department: (e.department as string) ?? "—",
    designation: (e.designation as string) ?? "—",
    salary: e.salary != null ? Number(e.salary) : null,
    hire_date: employeeHireDate(e) ?? "—",
  }));
}

function EmployeesPage() {
  const { data, isLoading, isError, refetch } = useQuery({
    queryKey: ["employees"],
    queryFn: services.employees,
    staleTime: 60_000,
  });

  return (
    <div className="max-w-7xl mx-auto flex flex-col gap-6">
      <div>
        <div className="text-xs uppercase tracking-widest text-muted-foreground">
          Directory
        </div>
        <h1 className="text-3xl font-bold gradient-text mt-1">Employees</h1>
      </div>

      {isLoading ? (
        <Card>
          <div className="flex flex-col gap-3">
            {Array.from({ length: 8 }).map((_, i) => (
              <Skeleton key={i} className="h-10 w-full" />
            ))}
          </div>
        </Card>
      ) : isError ? (
        <ErrorState onRetry={() => refetch()} description="Failed to load employees." />
      ) : (
        <DataTable
          data={normalize(data ?? [])}
          columns={columns}
          pageSize={12}
        />
      )}
    </div>
  );
}
