import { createFileRoute } from "@tanstack/react-router";
import { ExternalLink, FileCode2, BookOpen, Braces } from "lucide-react";
import { Card } from "@/components/ui-kit/Card";
import { Button } from "@/components/ui-kit/Button";
import { getBaseUrl } from "@/lib/config";
import { useState, useEffect } from "react";

export const Route = createFileRoute("/docs")({
  component: DocsPage,
});

function DocsPage() {
  const [base, setBase] = useState("");
  useEffect(() => setBase(getBaseUrl()), []);

  const open = (path: string) => window.open(`${base}${path}`, "_blank", "noopener,noreferrer");

  return (
    <div className="max-w-4xl mx-auto flex flex-col gap-6">
      <div>
        <div className="text-xs uppercase tracking-widest text-muted-foreground">
          Reference
        </div>
        <h1 className="text-3xl font-bold gradient-text mt-1">API Documentation</h1>
        <p className="text-muted-foreground text-sm mt-1">
          Interactive FastAPI docs served from your backend.
        </p>
      </div>

      <div className="grid sm:grid-cols-3 gap-4">
        <Card className="flex flex-col gap-3">
          <div className="h-10 w-10 rounded-xl gradient-brand grid place-items-center">
            <FileCode2 className="h-5 w-5 text-white" />
          </div>
          <h3 className="font-semibold">Swagger UI</h3>
          <p className="text-sm text-muted-foreground">
            Try requests directly from your browser.
          </p>
          <Button onClick={() => open("/docs")}>
            Open Swagger <ExternalLink className="h-4 w-4" />
          </Button>
        </Card>

        <Card className="flex flex-col gap-3">
          <div className="h-10 w-10 rounded-xl gradient-brand grid place-items-center">
            <BookOpen className="h-5 w-5 text-white" />
          </div>
          <h3 className="font-semibold">ReDoc</h3>
          <p className="text-sm text-muted-foreground">
            Clean, three-panel API reference.
          </p>
          <Button variant="secondary" onClick={() => open("/redoc")}>
            Open ReDoc <ExternalLink className="h-4 w-4" />
          </Button>
        </Card>

        <Card className="flex flex-col gap-3">
          <div className="h-10 w-10 rounded-xl gradient-brand grid place-items-center">
            <Braces className="h-5 w-5 text-white" />
          </div>
          <h3 className="font-semibold">OpenAPI JSON</h3>
          <p className="text-sm text-muted-foreground">
            Raw machine-readable schema.
          </p>
          <Button variant="outline" onClick={() => open("/openapi.json")}>
            Open JSON <ExternalLink className="h-4 w-4" />
          </Button>
        </Card>
      </div>

      <Card>
        <div className="text-xs text-muted-foreground">Currently pointing to</div>
        <div className="font-mono text-sm mt-1 break-all">{base || "…"}</div>
      </Card>
    </div>
  );
}
