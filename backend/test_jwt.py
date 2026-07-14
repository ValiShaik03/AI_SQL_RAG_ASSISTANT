from services.jwt_service import (
    create_access_token,
    verify_token
)

token = create_access_token(
    {
        "user_id": 1,
        "email": "admin@company.com",
        "role": "Admin"
    }
)

print("Generated Token:\n")
print(token)

print("\nDecoded Payload:\n")
print(
    verify_token(token)
)