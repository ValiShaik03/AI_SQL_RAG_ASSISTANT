from services.audit_service import log_activity

log_activity(
    user_id=1,
    action="TEST",
    description="Audit logging is working."
)

print("Audit log inserted successfully.")