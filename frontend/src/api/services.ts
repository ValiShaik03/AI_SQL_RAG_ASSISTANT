// Generated services.ts
import { api } from "./axios";

export interface HealthResponse {
  status?: string;
  database?: string;
  [k: string]: unknown;
}

export interface DashboardResponse {
  employees?: number;
  avg_salary?: number;
  max_salary?: number;
  departments?: number;
  [k: string]: unknown;
}

export interface InsightsResponse {
  highest_paid_department?: { department?: string; avg_salary?: number };
  lowest_paid_department?: { department?: string; avg_salary?: number };
  average_salary?: number;
  latest_hiring_year?: number;
  total_employees?: number;
  [k: string]: unknown;
}

export interface Employee {
  id?: number | string;
  employee_id?: number | string;
  employeeId?: number | string;
  name?: string;
  first_name?: string;
  firstName?: string;
  last_name?: string;
  lastName?: string;
  email?: string;
  department?: string;
  designation?: string;
  salary?: number;
  hire_date?: string;
  hireDate?: string;
  [k: string]: unknown;
}

export interface ChatResponse {
  status?: string;
  question?: string;
  generated_sql?: string;
  sql?: string;
  query?: string;
  answer?: string;
  columns?: string[];
  rows_returned?: number;
  execution_time_ms?: number;
  data?: Array<Record<string, unknown>>;
  results?: Array<Record<string, unknown>>;
  error?: string;
  message?: string;
  detail?: string;
  [k: string]: unknown;
}

export interface DbStatsResponse {
  database?: string;
  total_tables?: number;
  total_rows?: number;
  total_columns?: number;
  tables?: Array<{ table: string; rows: number; columns: number }>;
  [k: string]: unknown;
}

export interface LoginResponse {
  status?: string;
  message?: string;
  access_token?: string;
  token?: string;
  token_type?: string;
  user?: {
    id?: number | string;
    name?: string;
    full_name?: string;
    email?: string;
    role?: string;
    [k: string]: unknown;
  };
  [k: string]: unknown;
}

export interface User {
  user_id: number;
  full_name: string;
  email: string;
  role: string;
  is_active: boolean | number;
  created_at: string;
}

export interface UsersResponse {
  status: string;
  users: User[];
}

const unwrap = <T,>(d:any, keys:string[]):T=>{
 if(Array.isArray(d)) return d as T;
 for(const k of keys) if(d && Array.isArray(d[k])) return d[k] as T;
 return d as T;
};

export const services = {
  health:()=>api.get<HealthResponse>("/health").then(r=>r.data),
  login:(email:string,password:string)=>api.post<LoginResponse>("/api/auth/login",{email,password}).then(r=>r.data),
  dashboard:()=>api.get("/analytics/dashboard").then(r=>r.data),
  insights:()=>api.get("/analytics/insights").then(r=>r.data),
  dbStats:()=>api.get<DbStatsResponse>("/database/stats").then(r=>r.data),
  databaseTables:()=>api.get("/database/tables").then(r=>r.data),
  tableInfo:(table:string)=>api.get(`/database/info/${table}`).then(r=>r.data),
  tableSchema:(table:string)=>api.get(`/database/schema/${table}`).then(r=>r.data),
  schemaSummary:(table:string)=>api.get(`/database/schema-summary/${table}`).then(r=>r.data),
  tablePreview:(table:string,page=1,page_size=10)=>api.get(`/database/preview/${table}`,{params:{page,page_size}}).then(r=>r.data),
  relationships:()=>api.get("/database/relationships").then(r=>r.data),
  employees:()=>api.get("/employees").then(r=>unwrap<Employee[]>(r.data,["employees","data"])),
  chat:(question:string)=>api.post<ChatResponse>("/api/chat",{question}).then(r=>r.data),
  history:()=>api.get("/api/history").then(r=>r.data),
  deleteHistory:(historyId:number)=>api.delete(`/api/history/${historyId}`).then(r=>r.data),
  exportCsv:(columns:string[],data:Record<string,unknown>[])=>api.post("/api/export/csv",{columns,data},{responseType:"blob"}),
  exportExcel:(columns:string[],data:Record<string,unknown>[])=>api.post("/api/export/excel",{columns,data},{responseType:"blob"}),
  analyticsDepartments:()=>api.get("/analytics/departments").then(r=>unwrap<any[]>(r.data,["departments","data"])),
  analyticsSalary:()=>api.get("/analytics/salary").then(r=>unwrap<any[]>(r.data,["salary","data"])),
  analyticsHiring:()=>api.get("/analytics/hiring").then(r=>unwrap<any[]>(r.data,["hiring","trend","data"])),
  auditLogs:(page=1,page_size=10,action?:string,user_id?:number)=>api.get("/api/admin/audit-logs",{params:{page,page_size,action,user_id}}).then(r=>r.data),
    // -----------------------------
  // User Management
  // -----------------------------

  getUsers: () =>
    api.get<UsersResponse>("/api/admin/users").then((r) => r.data),

  createUser: (payload: {
    full_name: string;
    email: string;
    password: string;
    role: string;
  }) =>
    api.post("/api/admin/users", payload).then((r) => r.data),

  updateUser: (
    user_id: number,
    payload: {
      full_name: string;
      email: string;
      role: string;
    }
  ) =>
    api.put(`/api/admin/users/${user_id}`, payload).then((r) => r.data),

  deleteUser: (user_id: number) =>
    api.delete(`/api/admin/users/${user_id}`).then((r) => r.data),

  updateUserStatus: (user_id: number, is_active: boolean) =>
    api.patch(`/api/admin/users/${user_id}/status`, {
      is_active,
    }).then((r) => r.data),

  resetUserPassword: (
    user_id: number,
    new_password: string
  ) =>
    api.post(`/api/admin/users/${user_id}/reset-password`, {
      new_password,
    }).then((r) => r.data),
};

export function employeeDisplayName(e:Employee):string{
 if(e.name && String(e.name).trim()) return String(e.name);
 const full=`${e.first_name??e.firstName??""} ${e.last_name??e.lastName??""}`.trim();
 return full || (e.email as string) || "—";
}
export function employeeId(e:Employee){return e.id??e.employee_id??e.employeeId;}
export function employeeHireDate(e:Employee){return (e.hire_date??e.hireDate) as string|undefined;}
