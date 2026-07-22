import { useState } from "react";
import { useMutation } from "@tanstack/react-query";

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

import { KeyRound } from "lucide-react";

interface Props {
  user: any;
}

export function ResetPasswordDialog({ user }: Props) {
  const [open, setOpen] = useState(false);

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const mutation = useMutation({
    mutationFn: () =>
  services.resetUserPassword(user.user_id, password),

    onSuccess: () => {
      setOpen(false);
      setPassword("");
      setConfirmPassword("");
    },
  });

  const handleReset = () => {
    if (!password.trim()) {
      alert("Password is required");
      return;
    }

    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    mutation.mutate();
  };

  return (
  <Dialog open={open} onOpenChange={setOpen}>
    <DialogTrigger asChild>
      <Button variant="ghost" size="icon">
        <KeyRound className="h-4 w-4 text-amber-500" />
      </Button>
    </DialogTrigger>

    <DialogContent className="sm:max-w-md">
      <DialogHeader>
        <DialogTitle>Reset Password</DialogTitle>
      </DialogHeader>

      <div className="space-y-4 py-2">
        <p className="text-sm text-muted-foreground">
          Reset password for
          <span className="font-semibold text-foreground">
            {" "}
            {user.full_name}
          </span>
        </p>

        <Input
          type="password"
          placeholder="New Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Input
          type="password"
          placeholder="Confirm Password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
      </div>

      <DialogFooter className="gap-2">
        <Button
          variant="outline"
          onClick={() => setOpen(false)}
        >
          Cancel
        </Button>

        <Button
          onClick={handleReset}
          disabled={mutation.isPending}
        >
          {mutation.isPending
            ? "Resetting..."
            : "Reset Password"}
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
);
}