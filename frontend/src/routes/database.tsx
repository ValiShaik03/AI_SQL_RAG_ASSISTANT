
import { createFileRoute } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";
import { services } from "@/api/services";
import { Card } from "@/components/ui-kit/Card";
import { Loader } from "@/components/ui-kit/Loader";
import { ErrorState, EmptyState } from "@/components/ui-kit/States";
import { DataTable } from "@/components/ui-kit/DataTable";
import { Database } from "lucide-react";

export const Route = createFileRoute("/database")({
  component: DatabaseExplorer,
});

function DatabaseExplorer() {
  const [selected, setSelected] = useState<string | null>(null);

  const tables = useQuery({
    queryKey:["db-tables"],
    queryFn: services.databaseTables,
  });

  const info = useQuery({
    queryKey:["db-info",selected],
    queryFn:()=>services.tableInfo(selected!),
    enabled:!!selected
  });

  const schema = useQuery({
    queryKey:["db-schema",selected],
    queryFn:()=>services.tableSchema(selected!),
    enabled:!!selected
  });

  const summary = useQuery({
    queryKey:["db-summary",selected],
    queryFn:()=>services.schemaSummary(selected!),
    enabled:!!selected
  });

  const preview = useQuery({
    queryKey:["db-preview",selected],
    queryFn:()=>services.tablePreview(selected!,1,10),
    enabled:!!selected
  });

  const relations = useQuery({
    queryKey:["db-rel"],
    queryFn:services.relationships
  });

  if(tables.isLoading) return <Loader />;
  if(tables.isError) return <ErrorState title="Failed to load tables" description="Please try again." />;

  const list = tables.data?.tables ?? [];
  const rows = preview.data?.rows ?? [];
  const cols = rows.length ? Object.keys(rows[0]).map(k=>({key:k,label:k})) : [];

  return (
    <div className="grid grid-cols-[260px_1fr] gap-6">
      <Card>
        <h2 className="font-semibold mb-3 flex items-center gap-2"><Database className="h-4 w-4"/>Tables</h2>
        <div className="space-y-2">
          {list.map((t:string)=>(
            <button key={t}
              onClick={()=>setSelected(t)}
              className={`w-full text-left px-3 py-2 rounded-lg ${selected===t?"bg-primary text-white":"hover:bg-muted"}`}>
              {t}
            </button>
          ))}
        </div>
      </Card>

      <div className="space-y-4">
        {!selected && (
          <Card>
            <EmptyState
              icon={<Database className="h-6 w-6"/>}
              title="Select a table"
              description="Choose a table from the left panel."
            />
          </Card>
        )}

        {selected && (
          <>
            <Card>
              <h2 className="font-semibold mb-4">{selected}</h2>
              {info.isLoading ? <Loader/> :
              <div className="grid grid-cols-4 gap-4">
                <div><b>Rows</b><div>{info.data?.rows}</div></div>
                <div><b>Columns</b><div>{info.data?.columns}</div></div>
                <div><b>Primary Key</b><div>{info.data?.primary_key ?? "—"}</div></div>
                <div><b>Numeric</b><div>{summary.data?.numeric_columns}</div></div>
              </div>}
            </Card>

            <Card>
              <h3 className="font-semibold mb-3">Schema</h3>
              <DataTable
                data={schema.data?.schema ?? []}
                columns={[
                  {key:"Field",label:"Field"},
                  {key:"Type",label:"Type"},
                  {key:"Null",label:"Null"},
                  {key:"Key",label:"Key"},
                  {key:"Default",label:"Default"},
                ]}
              />
            </Card>

            <Card>
              <h3 className="font-semibold mb-3">Preview</h3>
              {rows.length===0 ? <EmptyState title="No rows" description="No data available." icon={<Database className="h-5 w-5"/>}/> :
              <DataTable data={rows} columns={cols} />}
            </Card>

            <Card>
              <h3 className="font-semibold mb-3">Relationships</h3>
              <DataTable
                data={relations.data?.relationships ?? []}
                columns={[
                  {key:"TABLE_NAME",label:"Table"},
                  {key:"COLUMN_NAME",label:"Column"},
                  {key:"REFERENCED_TABLE_NAME",label:"References"},
                  {key:"REFERENCED_COLUMN_NAME",label:"Reference Column"},
                ]}
              />
            </Card>
          </>
        )}
      </div>
    </div>
  );
}
