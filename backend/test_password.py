from utils.password import hash_password, verify_password

password = "Admin@123"

hashed = hash_password(password)

print("Original Password:")
print(password)

print("\nHashed Password:")
print(hashed)

print("\nVerification:")
print(
    verify_password(
        password,
        hashed
    )
)