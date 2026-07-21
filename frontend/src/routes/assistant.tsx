import { createFileRoute } from "@tanstack/react-router";
import { useMutation } from "@tanstack/react-query";
import { useEffect, useMemo, useRef, useState } from "react";
import {
  Send,
  Sparkles,
  Copy,
  Check,
  Loader2,
  ChevronDown,
  ChevronUp,
  Download,
  Search,
  History as HistoryIcon,
  Trash2,
  Clock,
  Database,
  Cpu,
  Rows3,
  CheckCircle2,
  AlertTriangle,
  User,
  Bot,
} from "lucide-react";
import { services, type ChatResponse } from "@/api/services";
import { Card } from "@/components/ui-kit/Card";
import { Button } from "@/components/ui-kit/Button";
import { useToast } from "@/components/ui-kit/Toast";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/assistant")({
  component: AssistantPage,
});

const EXAMPLES = [
  "Show top 5 highest salaries",
  "Average salary by department",
  "Employees hired after 2022",
  "Count employees",
];

const LOADING_STAGES = [
  "Thinking...",
  "Generating SQL...",
  "Executing Query...",
  "Generating AI Answer...",
];

const HISTORY_KEY = "sqlrag:history";

interface Turn {
  id: string;
  question: string;
  response?: ChatResponse;
  error?: string;
  pending?: boolean;
}

function loadHistory(): string[] {
  try {
    const raw = localStorage.getItem(HISTORY_KEY);
    if (!raw) return [];
    const arr = JSON.parse(raw);
    return Array.isArray(arr) ? arr.slice(0, 10) : [];
  } catch {
    return [];
  }
}

function saveHistory(list: string[]) {
  try {
    localStorage.setItem(HISTORY_KEY, JSON.stringify(list.slice(0, 10)));
  } catch {
    /* ignore */
  }
}

function extract(result: ChatResponse | undefined) {
  const rows = (result?.data ?? result?.results ?? []) as Array<Record<string, unknown>>;
  const columns =
    (result?.columns && result.columns.length ? result.columns : null) ??
    (Array.isArray(rows) && rows[0] ? Object.keys(rows[0] as object) : []);
  const sql = result?.generated_sql || result?.sql || result?.query || "";
  const answer = result?.answer || "";
  const statusStr = result?.status ? String(result.status).toLowerCase() : "";
  const SUCCESS_STATUSES = new Set(["success", "ok", "200", "completed", "done"]);
  const FAILURE_STATUSES = new Set(["failed", "error", "failure", "denied"]);
  const asStr = (v: unknown) =>
    typeof v === "string" ? v : v == null ? "" : typeof v === "object" ? "" : String(v);
  const explicitMsg =
    asStr((result as any)?.message) ||
    asStr(result?.error) ||
    asStr(result?.detail);
  const isFailure =
    !!explicitMsg && !statusStr
      ? true
      : statusStr
        ? FAILURE_STATUSES.has(statusStr) || (!SUCCESS_STATUSES.has(statusStr) && !!explicitMsg)
        : false;
  const backendError = isFailure
    ? explicitMsg || `Request ${statusStr || "failed"}`
    : "";
  return { rows, columns, sql, answer, backendError };
}

function toCSV(cols: string[], rows: Array<Record<string, unknown>>) {
  const esc = (v: unknown) => `"${String(v ?? "").replace(/"/g, '""')}"`;
  return [cols.join(","), ...rows.map((r) => cols.map((c) => esc(r[c])).join(","))].join("\n");
}

function AssistantPage() {
  const [question, setQuestion] = useState("");
  const [turns, setTurns] = useState<Turn[]>([]);
  const [history, setHistory] = useState<string[]>([]);
  const [stageIdx, setStageIdx] = useState(0);
  const toast = useToast();
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setHistory(loadHistory());
  }, []);

  const mutation = useMutation({
    mutationFn: async ({ q, id }: { q: string; id: string }) => {
      const res = await services.chat(q);
      return { id, res };
    },
    onSuccess: ({ id, res }, { q }) => {
      setTurns((t) =>
        t.map((x) => (x.id === id ? { ...x, response: res, pending: false } : x)),
      );
      setHistory((h) => {
        const next = [q, ...h.filter((x) => x !== q)].slice(0, 10);
        saveHistory(next);
        return next;
      });
    },
    onError: (e: any, { id }) => {
      // Only reached when the HTTP request itself fails (no response,
      // network error, timeout, or non-2xx). Backend logical failures
      // arrive as 200 with status:"failed" and are handled in extract().
      const noResponse = !e?.response;
      const msg = noResponse
        ? "Network error — could not reach the server. Please check your connection and try again."
        : e?.response?.data?.detail ||
          e?.response?.data?.message ||
          e?.message ||
          "Request failed";
      setTurns((t) => t.map((x) => (x.id === id ? { ...x, error: msg, pending: false } : x)));
      toast({ type: "error", message: msg });
    },
  });

  useEffect(() => {
    if (!mutation.isPending) return;
    setStageIdx(0);
    const iv = setInterval(
      () => setStageIdx((i) => (i + 1) % LOADING_STAGES.length),
      1400,
    );
    return () => clearInterval(iv);
  }, [mutation.isPending]);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [turns.length, mutation.isPending]);

  const submit = (q?: string) => {
    const query = (q ?? question).trim();
    if (!query || mutation.isPending) return;
    const id = `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
    setTurns((t) => [...t, { id, question: query, pending: true }]);
    setQuestion("");
    mutation.mutate({ q: query, id });
  };

  const clearChat = () => {
    setTurns([]);
  };

  const clearHistory = () => {
    setHistory([]);
    saveHistory([]);
  };

  return (
    <div className="max-w-7xl mx-auto flex flex-col gap-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <div className="text-xs uppercase tracking-widest text-muted-foreground">
            AI Assistant
          </div>
          <h1 className="text-3xl font-bold gradient-text mt-1">Ask your database</h1>
          <p className="text-muted-foreground text-sm mt-1">
            Natural language in. Real SQL and results out.
          </p>
        </div>
        {turns.length > 0 && (
          <Button variant="ghost" size="sm" onClick={clearChat}>
            <Trash2 className="h-4 w-4" /> New chat
          </Button>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-6 items-start">
        {/* History panel */}
        <Card className="flex flex-col gap-3 lg:sticky lg:top-4 max-h-[75vh]">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2 text-sm font-semibold">
              <HistoryIcon className="h-4 w-4 text-primary" />
              History
            </div>
            {history.length > 0 && (
              <button
                onClick={clearHistory}
                className="text-xs text-muted-foreground hover:text-foreground"
                title="Clear history"
              >
                Clear
              </button>
            )}
          </div>
          {history.length === 0 ? (
            <div className="text-xs text-muted-foreground py-6 text-center">
              Your last 10 questions will appear here.
            </div>
          ) : (
            <div className="flex flex-col gap-1 overflow-y-auto -mx-1 px-1">
              {history.map((h) => (
                <button
                  key={h}
                  onClick={() => submit(h)}
                  className="text-left text-xs px-3 py-2 rounded-lg hover:bg-muted/60 text-muted-foreground hover:text-foreground truncate transition"
                  title={h}
                >
                  {h}
                </button>
              ))}
            </div>
          )}
          <div className="border-t border-border pt-3 mt-1">
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground mb-2">
              Try
            </div>
            <div className="flex flex-col gap-1">
              {EXAMPLES.map((ex) => (
                <button
                  key={ex}
                  onClick={() => submit(ex)}
                  className="text-left text-xs px-3 py-2 rounded-lg border border-border hover:border-primary hover:text-primary transition"
                >
                  {ex}
                </button>
              ))}
            </div>
          </div>
        </Card>

        {/* Chat area */}
        <div className="flex flex-col gap-4 min-w-0">
          <div
            ref={scrollRef}
            className="flex flex-col gap-6 min-h-[300px] max-h-[65vh] overflow-y-auto pr-1"
          >
            {turns.length === 0 && !mutation.isPending && (
              <Card className="flex flex-col items-center text-center py-12 gap-3">
                <div className="h-12 w-12 rounded-2xl gradient-brand grid place-items-center shadow-lg shadow-primary/30">
                  <Sparkles className="h-6 w-6 text-white" />
                </div>
                <h3 className="font-semibold">Ask anything about your data</h3>
                <p className="text-sm text-muted-foreground max-w-md">
                  Try one of the examples on the left, or type your own question below.
                </p>
              </Card>
            )}

            {turns.map((t) => (
              <TurnView key={t.id} turn={t} loadingLabel={LOADING_STAGES[stageIdx]} />
            ))}
          </div>

          {/* Composer */}
          <Card className="flex flex-col gap-3">
            <div className="flex items-center gap-2 text-xs font-medium text-muted-foreground uppercase tracking-wider">
              <Sparkles className="h-3.5 w-3.5 text-primary" />
              Your question
            </div>
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  submit();
                }
              }}
              rows={2}
              placeholder="e.g. Show top 5 highest paid employees in Engineering"
              className="w-full rounded-xl bg-muted/50 border border-border p-3 text-sm outline-none focus:border-primary transition resize-none"
            />
            <div className="flex items-center justify-between gap-3">
              <div className="text-xs text-muted-foreground">
                Enter to send · Shift+Enter for newline
              </div>
              <Button
                onClick={() => submit()}
                disabled={mutation.isPending || !question.trim()}
              >
                {mutation.isPending ? (
                  <Loader2 className="h-4 w-4 animate-spin" />
                ) : (
                  <Send className="h-4 w-4" />
                )}
                Ask
              </Button>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}

function TurnView({ turn, loadingLabel }: { turn: Turn; loadingLabel: string }) {
  return (
    <div className="flex flex-col gap-3">
      <UserBubble text={turn.question} />
      {turn.pending ? (
        <AssistantBubble>
          <div className="flex items-center gap-2 text-sm text-muted-foreground">
            <Loader2 className="h-4 w-4 animate-spin text-primary" />
            <span className="animate-pulse">{loadingLabel}</span>
          </div>
        </AssistantBubble>
      ) : turn.error ? (
        <AssistantBubble>
          <ErrorCard title="Query failed" message={turn.error} />
        </AssistantBubble>
      ) : turn.response ? (
        <AssistantResponse response={turn.response} question={turn.question} />
      ) : null}
    </div>
  );
}

function UserBubble({ text }: { text: string }) {
  return (
    <div className="flex items-start gap-3 justify-end">
      <div className="max-w-[85%] rounded-2xl rounded-tr-sm px-4 py-3 text-sm gradient-brand text-white shadow-lg shadow-primary/20">
        {text}
      </div>
      <div className="h-8 w-8 shrink-0 rounded-full bg-muted grid place-items-center text-muted-foreground">
        <User className="h-4 w-4" />
      </div>
    </div>
  );
}

function AssistantBubble({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex items-start gap-3">
      <div className="h-8 w-8 shrink-0 rounded-full gradient-brand grid place-items-center shadow-lg shadow-primary/20">
        <Bot className="h-4 w-4 text-white" />
      </div>
      <div className="flex-1 min-w-0 flex flex-col gap-3">{children}</div>
    </div>
  );
}

function AssistantResponse({
  response,
  question,
}: {
  response: ChatResponse;
  question: string;
}) {
  const { rows, columns, sql, answer, backendError } = useMemo(
    () => extract(response),
    [response],
  );
  const status = backendError ? "error" : "success";
  const execMs = response.execution_time_ms;
  const rowsReturned = response.rows_returned ?? (Array.isArray(rows) ? rows.length : 0);

  return (
    <AssistantBubble>
      {answer ? (
        <div className="rounded-2xl rounded-tl-sm bg-muted/50 border border-border px-4 py-3 text-sm leading-relaxed">
          {answer}
        </div>
      ) : !backendError ? (
        <div className="rounded-2xl rounded-tl-sm bg-muted/50 border border-border px-4 py-3 text-sm text-muted-foreground">
          Query executed successfully.
        </div>
      ) : null}

      {backendError && <ErrorCard title="Backend error" message={backendError} />}

      {sql && <SqlBlock sql={sql} />}

      <StatsRow
        execMs={execMs}
        rows={rowsReturned}
        status={status}
      />

      {Array.isArray(rows) && rows.length > 0 && columns.length > 0 && (
        <ResultsTable rows={rows} columns={columns} filename={sanitize(question)} />
      )}
    </AssistantBubble>
  );
}

function ErrorCard({ title, message }: { title: string; message: string }) {
  return (
    <div className="rounded-2xl border border-destructive/40 bg-destructive/10 p-4 flex items-start gap-3">
      <div className="h-8 w-8 shrink-0 rounded-full bg-destructive/20 text-destructive grid place-items-center">
        <AlertTriangle className="h-4 w-4" />
      </div>
      <div className="flex flex-col gap-1 min-w-0">
        <div className="text-sm font-semibold">{title}</div>
        <div className="text-xs text-muted-foreground break-words">{message}</div>
      </div>
    </div>
  );
}

function SqlBlock({ sql }: { sql: string }) {
  const [copied, setCopied] = useState(false);
  const [open, setOpen] = useState(true);

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(sql);
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    } catch {
      /* ignore */
    }
  };

  return (
    <div className="rounded-2xl border border-border bg-muted/40 overflow-hidden">
      <div className="flex items-center justify-between px-4 py-2 border-b border-border bg-muted/60">
        <div className="flex items-center gap-2 text-xs font-medium">
          <span className="h-2 w-2 rounded-full bg-primary" />
          Generated SQL
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={copy}
            className="text-xs inline-flex items-center gap-1 text-muted-foreground hover:text-foreground"
          >
            {copied ? <Check className="h-3 w-3" /> : <Copy className="h-3 w-3" />}
            {copied ? "Copied" : "Copy"}
          </button>
          <button
            onClick={() => setOpen((v) => !v)}
            className="text-xs inline-flex items-center gap-1 text-muted-foreground hover:text-foreground"
          >
            {open ? <ChevronUp className="h-3 w-3" /> : <ChevronDown className="h-3 w-3" />}
            {open ? "Collapse" : "Expand"}
          </button>
        </div>
      </div>
      {open && (
        <pre className="p-4 text-xs overflow-auto font-mono max-h-72 whitespace-pre-wrap leading-relaxed">
          <SqlHighlighted sql={sql} />
        </pre>
      )}
    </div>
  );
}

const SQL_KEYWORDS = new Set([
  "SELECT","FROM","WHERE","JOIN","LEFT","RIGHT","INNER","OUTER","ON","AND","OR","NOT",
  "GROUP","BY","ORDER","HAVING","LIMIT","OFFSET","AS","DISTINCT","IN","IS","NULL",
  "COUNT","SUM","AVG","MIN","MAX","CASE","WHEN","THEN","ELSE","END","INSERT","INTO",
  "UPDATE","SET","DELETE","VALUES","CREATE","TABLE","DROP","ALTER","WITH","UNION","ALL",
  "BETWEEN","LIKE","DESC","ASC",
]);

function SqlHighlighted({ sql }: { sql: string }) {
  const tokens = sql.split(/(\s+|,|\(|\)|;)/);
  return (
    <>
      {tokens.map((tok, i) => {
        const up = tok.toUpperCase();
        if (SQL_KEYWORDS.has(up))
          return (
            <span key={i} className="text-primary font-semibold">
              {tok}
            </span>
          );
        if (/^'[^']*'$|^"[^"]*"$/.test(tok))
          return (
            <span key={i} className="text-emerald-400">
              {tok}
            </span>
          );
        if (/^\d+(\.\d+)?$/.test(tok))
          return (
            <span key={i} className="text-amber-400">
              {tok}
            </span>
          );
        return <span key={i}>{tok}</span>;
      })}
    </>
  );
}

function StatsRow({
  execMs,
  rows,
  status,
}: {
  execMs?: number;
  rows: number;
  status: "success" | "error";
}) {
  const items = [
    {
      label: "Execution Time",
      value: execMs != null ? `${Number(execMs).toFixed(0)} ms` : "—",
      icon: <Clock className="h-3.5 w-3.5" />,
    },
    {
      label: "Rows Returned",
      value: rows.toLocaleString(),
      icon: <Rows3 className="h-3.5 w-3.5" />,
    },
    {
      label: "Database",
      value: "MySQL",
      icon: <Database className="h-3.5 w-3.5" />,
    },
    {
      label: "AI Model",
      value: "Llama 3.3 70B",
      icon: <Cpu className="h-3.5 w-3.5" />,
    },
    {
      label: "Status",
      value: status === "success" ? "Success" : "Error",
      icon:
        status === "success" ? (
          <CheckCircle2 className="h-3.5 w-3.5 text-[color:var(--success)]" />
        ) : (
          <AlertTriangle className="h-3.5 w-3.5 text-destructive" />
        ),
    },
  ];
  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2">
      {items.map((it) => (
        <div
          key={it.label}
          className="rounded-xl border border-border bg-muted/40 p-3 flex flex-col gap-1 hover:border-primary/40 hover:bg-muted/60 transition"
        >
          <div className="flex items-center gap-1.5 text-[10px] uppercase tracking-wider text-muted-foreground">
            {it.icon}
            {it.label}
          </div>
          <div className="text-sm font-semibold truncate">{it.value}</div>
        </div>
      ))}
    </div>
  );
}

function ResultsTable({
  rows,
  columns,
  filename,
}: {
  rows: Array<Record<string, unknown>>;
  columns: string[];
  filename: string;
}) {
  const [query, setQuery] = useState("");
  const [sortKey, setSortKey] = useState<string | null>(null);
  const [sortDir, setSortDir] = useState<"asc" | "desc">("asc");
  const [page, setPage] = useState(1);
  const pageSize = 10;

  const filtered = useMemo(() => {
    let out = rows;
    if (query) {
      const q = query.toLowerCase();
      out = out.filter((r) =>
        columns.some((c) => String(r[c] ?? "").toLowerCase().includes(q)),
      );
    }
    if (sortKey) {
      out = [...out].sort((a, b) => {
        const va = a[sortKey];
        const vb = b[sortKey];
        if (va == null) return 1;
        if (vb == null) return -1;
        const na = Number(va);
        const nb = Number(vb);
        if (Number.isFinite(na) && Number.isFinite(nb))
          return sortDir === "asc" ? na - nb : nb - na;
        return sortDir === "asc"
          ? String(va).localeCompare(String(vb))
          : String(vb).localeCompare(String(va));
      });
    }
    return out;
  }, [rows, columns, query, sortKey, sortDir]);

  const pageCount = Math.max(1, Math.ceil(filtered.length / pageSize));
  const current = Math.min(page, pageCount);
  const pageRows = filtered.slice((current - 1) * pageSize, current * pageSize);

  const exportCSV = () => {
    const csv = toCSV(columns, filtered);
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${filename || "results"}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="rounded-2xl border border-border bg-muted/30 flex flex-col gap-3 p-3">
      <div className="flex items-center gap-2 flex-wrap justify-between">
        <div className="relative flex-1 min-w-[180px] max-w-xs">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted-foreground" />
          <input
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
              setPage(1);
            }}
            placeholder="Search results..."
            className="w-full h-9 rounded-lg bg-background/60 border border-border pl-8 pr-3 text-xs outline-none focus:border-primary transition"
          />
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs text-muted-foreground">
            {filtered.length.toLocaleString()} rows
          </span>
          <Button size="sm" variant="outline" onClick={exportCSV}>
            <Download className="h-3.5 w-3.5" /> CSV
          </Button>
        </div>
      </div>

      <div className="rounded-xl border border-border overflow-hidden bg-background/40">
        <div className="overflow-x-auto max-h-[420px] overflow-y-auto">
          <table className="w-full text-sm">
            <thead className="bg-muted/70 text-xs uppercase tracking-wider text-muted-foreground sticky top-0 z-10 backdrop-blur">
              <tr>
                {columns.map((c) => (
                  <th key={c} className="text-left px-4 py-2.5 font-medium whitespace-nowrap">
                    <button
                      className="inline-flex items-center gap-1 hover:text-foreground"
                      onClick={() => {
                        if (sortKey === c) setSortDir(sortDir === "asc" ? "desc" : "asc");
                        else {
                          setSortKey(c);
                          setSortDir("asc");
                        }
                      }}
                    >
                      {c}
                      {sortKey === c &&
                        (sortDir === "asc" ? (
                          <ChevronUp className="h-3 w-3" />
                        ) : (
                          <ChevronDown className="h-3 w-3" />
                        ))}
                    </button>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {pageRows.map((r, i) => (
                <tr key={i} className="border-t border-border hover:bg-muted/40 transition-colors">
                  {columns.map((c) => (
                    <td key={c} className="px-4 py-2.5 whitespace-nowrap">
                      {String(r[c] ?? "—")}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {pageCount > 1 && (
        <div className="flex items-center justify-between text-xs text-muted-foreground">
          <span>
            Page {current} of {pageCount}
          </span>
          <div className="flex gap-2">
            <button
              onClick={() => setPage(Math.max(1, current - 1))}
              disabled={current === 1}
              className={cn(
                "px-3 h-7 rounded-lg border border-border hover:bg-muted disabled:opacity-40",
              )}
            >
              Prev
            </button>
            <button
              onClick={() => setPage(Math.min(pageCount, current + 1))}
              disabled={current === pageCount}
              className={cn(
                "px-3 h-7 rounded-lg border border-border hover:bg-muted disabled:opacity-40",
              )}
            >
              Next
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

function sanitize(s: string) {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 40);
}
