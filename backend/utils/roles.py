from fastapi import Depends, HTTPException, status

from utils.auth import get_current_user


# ---------------------------------------------------------
# Generic Role Checker
# ---------------------------------------------------------

def require_role(allowed_roles: list[str]):
    """
    Generic RBAC dependency.

    Example:
        Depends(require_role(["Admin"]))
        Depends(require_role(["Admin", "Manager"]))
    """

    def role_checker(current_user=Depends(get_current_user)):
        role = current_user.get("role")

        if role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource."
            )

        return current_user

    return role_checker


# ---------------------------------------------------------
# Ready-to-use dependencies
# ---------------------------------------------------------

require_admin = require_role([
    "Admin"
])

require_manager = require_role([
    "Admin",
    "Manager"
])

require_analyst = require_role([
    "Admin",
    "Manager",
    "Analyst"
])

require_viewer = require_role([
    "Admin",
    "Manager",
    "Analyst",
    "Viewer"
])