import { useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { services } from "@/api/services";

import { Button } from "@/components/ui/button";

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogTrigger,
} from "@/components/ui/dialog";

import { Trash2 } from "lucide-react";

interface Props {
  user: any;
}

export function DeleteUserDialog({ user }: Props) {
  const [open, setOpen] = useState(false);

  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: () => services.deleteUser(user.user_id),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["users"],
      });

      setOpen(false);
    },
  });

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="ghost" size="icon">
          <Trash2 className="h-4 w-4 text-red-500" />
        </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Delete User</DialogTitle>
        </DialogHeader>

        <div className="py-2 text-sm text-muted-foreground">
          Are you sure you want to delete
          <span className="font-semibold text-foreground">
            {" "}
            {user.full_name}
          </span>
          ?
          <br />
          <br />
          This action cannot be undone.
        </div>

        <DialogFooter className="gap-2">
          <Button
            variant="outline"
            onClick={() => setOpen(false)}
          >
            Cancel
          </Button>

          <Button
            variant="destructive"
            onClick={() => mutation.mutate()}
            disabled={mutation.isPending}
          >
            {mutation.isPending ? "Deleting..." : "Delete User"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}