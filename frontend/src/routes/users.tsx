import { createFileRoute } from "@tanstack/react-router";
import { Card } from "@/components/ui-kit/Card";
//import { EmptyState } from "@/components/ui-kit/States";
import { ProtectedRoute } from "@/components/auth/ProtectedRoute";
//import { Users } from "lucide-react";
import { useQuery } from "@tanstack/react-query";

import { services } from "@/api/services";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { useMemo, useState } from "react";
import {
  Avatar,
  AvatarFallback,
} from "@/components/ui/avatar";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import {
  Search,
  UserPlus,
  Pencil,
  Trash2,
  KeyRound,
} from "lucide-react";


export const Route = createFileRoute("/users")({
  component: () => (
    <ProtectedRoute roles={["admin", "administrator"]}>
      <UserManagement />
    </ProtectedRoute>
  ),
});

function UserManagement() {

  const {
    data,
    isLoading,
    error,
    refetch,
  } = useQuery({
    queryKey: ["users"],
    queryFn: services.getUsers,
  });
  const [search, setSearch] = useState("");
  const filteredUsers = useMemo(() => {
  if (!data?.users) return [];

  const value = search.toLowerCase();

  return data.users.filter((user) => {
    return (
      user.full_name.toLowerCase().includes(value) ||
      user.email.toLowerCase().includes(value) ||
      user.role.toLowerCase().includes(value)
    );
  });
}, [data?.users, search]);
  if (isLoading) {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">User Management</h1>
        <p className="text-sm text-muted-foreground">
          Manage user accounts, roles and access.
        </p>
      </div>

      <Card className="p-6">
        <div className="space-y-4">
          <div className="h-10 w-72 animate-pulse rounded-md bg-muted" />

          {[1, 2, 3, 4].map((i) => (
            <div
              key={i}
              className="h-16 animate-pulse rounded-md bg-muted"
            />
          ))}
        </div>
      </Card>
    </div>
  );
}

  if (error) {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">User Management</h1>
        <p className="text-sm text-muted-foreground">
          Manage user accounts, roles and access.
        </p>
      </div>

      <Card className="p-6 flex flex-col items-center gap-4">
        <p className="text-red-500">
          Failed to load users.
        </p>

        <Button onClick={() => refetch()}>
          Retry
        </Button>
      </Card>
    </div>
  );
}

  if (!data?.users?.length) {
    return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">User Management</h1>
        <p className="text-sm text-muted-foreground">
          Manage user accounts, roles and access.
        </p>
      </div>

      <Card className="p-10 text-center">
        <h3 className="text-lg font-semibold">
          No Users Found
        </h3>

        <p className="text-muted-foreground">
          Create your first user.
        </p>
      </Card>
    </div>
  );
}

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">
          User Management
        </h1>

        <p className="text-sm text-muted-foreground">
          Manage user accounts, roles and access.
        </p>
      </div>

      <Card className="p-6 space-y-6">

  <div className="flex items-center justify-between">

    <div className="relative w-80">

      <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />

      <Input
        placeholder="Search users..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="pl-10"
      />

    </div>

    <Button disabled>
      <UserPlus className="mr-2 h-4 w-4" />
      Add User
    </Button>

  </div>

  <Table>

    <TableHeader>

      <TableRow>

        <TableHead>User</TableHead>
        <TableHead>Email</TableHead>
        <TableHead>Role</TableHead>
        <TableHead>Status</TableHead>
        <TableHead>Created</TableHead>
        <TableHead className="text-right">
          Actions
        </TableHead>

      </TableRow>

    </TableHeader>

    <TableBody>

      {filteredUsers.map((user) => (

        <TableRow key={user.user_id}>

          <TableCell>
            <div className="flex items-center gap-3">
              <Avatar className="h-9 w-9">
                <AvatarFallback>
                  {user.full_name
                    .split(" ")
                    .map((name) => name[0])
                    .join("")
                    .substring(0, 2)
                    .toUpperCase()}
                </AvatarFallback>
              </Avatar>

              <span className="font-medium">
                {user.full_name}
              </span>
            </div>
          </TableCell>

          <TableCell>
            {user.email}
          </TableCell>

          <TableCell>
              <Badge
              className={
                user.role.toLowerCase() === "admin"
                  ? "bg-red-500 hover:bg-red-600 text-white"
                  : user.role.toLowerCase() === "manager"
                  ? "bg-purple-500 hover:bg-purple-600 text-white"
                  : user.role.toLowerCase() === "analyst"
                  ? "bg-sky-500 hover:bg-sky-600 text-white"
                  : user.role.toLowerCase() === "viewer"
                  ? "bg-teal-500 hover:bg-teal-600 text-white"
                  : "bg-gray-500 hover:bg-gray-600 text-white"
              }
            >
              {user.role}
            </Badge>
          </TableCell>

          <TableCell>
              <Badge
                variant={user.is_active ? "default" : "secondary"}
                className={
                  user.is_active
                    ? "bg-emerald-600 hover:bg-emerald-700 text-white"
                    : "bg-red-600 hover:bg-red-700 text-white"
                }
              >
                {user.is_active ? "Active" : "Inactive"}
              </Badge>
          </TableCell>

          <TableCell>
              {new Date(user.created_at).toLocaleDateString("en-IN", {
                day: "2-digit",
                month: "short",
                year: "numeric",
              })}
          </TableCell>

          <TableCell className="text-right">
            <div className="flex items-center justify-end gap-1">

                <Button
                  variant="ghost"
                  size="icon"
                  disabled
                >
                  <Pencil className="h-4 w-4" />
                </Button>

                <Button
                  variant="ghost"
                  size="icon"
                  disabled
                >
                  <Trash2 className="h-4 w-4" />
                </Button>

                <Button
                  variant="ghost"
                  size="icon"
                  disabled
                >
                  <KeyRound className="h-4 w-4" />
                </Button>

              </div>
            </TableCell>
        </TableRow>

      ))}

    </TableBody>

  </Table>

</Card>
    </div>
  );
}