import { useEffect, useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { services, User } from "@/api/services";

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

import { Pencil } from "lucide-react";

interface Props {
  user: User;
}

export function EditUserDialog({ user }: Props) {
  const queryClient = useQueryClient();

  const [open, setOpen] = useState(false);

  const [fullName, setFullName] = useState(user.full_name);
  const [email, setEmail] = useState(user.email);
  const [role, setRole] = useState(user.role);

  useEffect(() => {
    if (open) {
      setFullName(user.full_name);
      setEmail(user.email);
      setRole(user.role);
    }
  }, [open, user]);

  const mutation = useMutation({
    mutationFn: (payload: {
      full_name: string;
      email: string;
      role: string;
    }) =>
      services.updateUser(user.user_id, payload),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["users"],
      });

      setOpen(false);

      alert("User updated successfully");
    },

    onError: (error: any) => {
      alert(
        error?.response?.data?.message ||
        "Failed to update user"
      );
    },
  });

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="ghost" size="icon">
          <Pencil className="h-4 w-4" />
        </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Edit User</DialogTitle>
        </DialogHeader>

        <div className="grid gap-4 py-2">

          <Input
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />

          <Input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
            disabled={mutation.isPending}
            onClick={() =>
              mutation.mutate({
                full_name: fullName.trim(),
                email: email.trim(),
                role,
              })
            }
          >
            {mutation.isPending ? "Updating..." : "Update User"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}