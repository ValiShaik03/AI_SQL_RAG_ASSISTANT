import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import {
  DEFAULT_BASE_URL,
  getBaseUrl,
  getTheme,
  setBaseUrl,
  setTheme,
  type Theme,
} from "@/lib/config";
import { Card } from "@/components/ui-kit/Card";
import { Button } from "@/components/ui-kit/Button";
import { useToast } from "@/components/ui-kit/Toast";
import { Moon, Sun, RotateCcw, Save, LogOut, ShieldCheck, ShieldAlert } from "lucide-react";
import { clearAuth, getToken, getUser, userDisplayName } from "@/lib/auth";

export const Route = createFileRoute("/settings")({
  component: SettingsPage,
});

function SettingsPage() {
  const [url, setUrl] = useState("");
  const [theme, setThemeState] = useState<Theme>("dark");
  const [hasToken, setHasToken] = useState(false);
  const [user, setUser] = useState(() => getUser());
  const toast = useToast();
  const navigate = useNavigate();

  useEffect(() => {
    setUrl(getBaseUrl());
    setThemeState(getTheme());
    setHasToken(!!getToken());
    setUser(getUser());
  }, []);

  const save = () => {
    setBaseUrl(url.trim() || DEFAULT_BASE_URL);
    toast({ type: "success", message: "Backend URL saved" });
  };

  const reset = () => {
    setUrl(DEFAULT_BASE_URL);
    setBaseUrl(DEFAULT_BASE_URL);
    toast({ type: "success", message: "Backend URL reset" });
  };

  const changeTheme = (t: Theme) => {
    setThemeState(t);
    setTheme(t);
  };

  const logout = () => {
    clearAuth();
    toast({ type: "success", message: "Signed out." });
    navigate({ to: "/login" });
  };

  return (
    <div className="max-w-3xl mx-auto flex flex-col gap-6">
      <div>
        <div className="text-xs uppercase tracking-widest text-muted-foreground">Preferences</div>
        <h1 className="text-3xl font-bold gradient-text mt-1">Settings</h1>
      </div>

      <Card className="flex flex-col gap-4">
        <h3 className="font-semibold">Session</h3>
        <div className="grid sm:grid-cols-2 gap-3 text-sm">
          <Info label="Current User" value={userDisplayName(user)} />
          <Info label="Email" value={(user?.email as string) || "—"} mono />
          <Info label="Role" value={(user?.role as string) || "—"} />
          <div className="flex flex-col gap-1">
            <span className="text-xs uppercase tracking-wider text-muted-foreground">JWT Status</span>
            <span className={`inline-flex items-center gap-1.5 text-sm font-medium ${hasToken ? "text-[color:var(--success)]":"text-destructive"}`}>
              {hasToken ? <><ShieldCheck className="h-4 w-4"/>Active</> : <><ShieldAlert className="h-4 w-4"/>Missing</>}
            </span>
          </div>
        </div>
        <Button variant="outline" onClick={logout}><LogOut className="h-4 w-4"/>Logout</Button>
      </Card>

      <Card className="flex flex-col gap-4">
        <h3 className="font-semibold">Backend Base URL</h3>
        <input value={url} onChange={(e)=>setUrl(e.target.value)}
          className="w-full h-11 rounded-xl bg-muted/60 border border-border px-3 text-sm font-mono outline-none focus:border-primary"/>
        <div className="flex gap-2">
          <Button onClick={save}><Save className="h-4 w-4"/>Save</Button>
          <Button variant="outline" onClick={reset}><RotateCcw className="h-4 w-4"/>Reset</Button>
        </div>
      </Card>

      <Card className="flex flex-col gap-4">
        <h3 className="font-semibold">Theme</h3>
        <div className="grid grid-cols-2 gap-3">
          {(["dark","light"] as const).map(t=>(
            <button key={t} onClick={()=>changeTheme(t)}
              className={`p-4 rounded-xl border ${theme===t?"border-primary bg-primary/10":"border-border hover:bg-muted"}`}>
              <div className="flex items-center gap-2 font-medium capitalize">
                {t==="dark"?<Moon className="h-4 w-4"/>:<Sun className="h-4 w-4"/>}{t}
              </div>
            </button>
          ))}
        </div>
      </Card>
    </div>
  );
}

function Info({label,value,mono}:{label:string;value:string;mono?:boolean}){
 return <div className="flex flex-col gap-1"><span className="text-xs uppercase tracking-wider text-muted-foreground">{label}</span><span className={mono?"font-mono break-all text-sm":"text-sm"}>{value}</span></div>;
}
