import { useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { services } from "@/api/services";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogTrigger,
} from "@/components/ui/dialog";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

import { UserPlus } from "lucide-react";

export function AddUserDialog() {
  const queryClient = useQueryClient();

  const [open, setOpen] = useState(false);

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("Viewer");

  const mutation = useMutation({
    mutationFn: services.createUser,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["users"],
      });

      setOpen(false);

      setFullName("");
      setEmail("");
      setPassword("");
      setRole("User");
    },
  });

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>
          <UserPlus className="mr-2 h-4 w-4" />
          Add User
        </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Add User</DialogTitle>
        </DialogHeader>

        <div className="grid gap-4 py-2">

          <Input
            placeholder="Full Name"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />

          <Input
            placeholder="Email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <Input
            placeholder="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <Select value={role} onValueChange={setRole}>
            <SelectTrigger>
              <SelectValue />
            </SelectTrigger>

            <SelectContent>
              <SelectItem value="Admin">Admin</SelectItem>
              <SelectItem value="Manager">Manager</SelectItem>
              <SelectItem value="Analyst">Analyst</SelectItem>
              <SelectItem value="Viewer">Viewer</SelectItem>
            </SelectContent>
          </Select>

        </div>

        <DialogFooter>
          <Button
            className="w-full"
            onClick={() => {
            if (!fullName.trim()) {
                alert("Full Name is required");
                return;
            }

            if (!email.trim()) {
                alert("Email is required");
                return;
            }

            if (!password.trim()) {
                alert("Password is required");
                return;
            }

            mutation.mutate({
                full_name: fullName.trim(),
                email: email.trim(),
                password,
                role,
            });
            }}
            disabled={mutation.isPending}
          >
            {mutation.isPending ? "Creating..." : "Create User"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}