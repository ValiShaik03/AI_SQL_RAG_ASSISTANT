from fastapi import Depends, HTTPException, status

from utils.auth import get_current_user


def require_role(allowed_roles: list):

    def role_checker(current_user=Depends(get_current_user)):

        user_role = current_user.get("role")

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )

        return current_user

    return role_checker


def require_admin(current_user=Depends(get_current_user)):

    if current_user.get("role") != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required."
        )

    return current_user