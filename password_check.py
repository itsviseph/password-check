import getpass
import re

# Regex patterns
USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9]{3,15}$")
PASSWORD_REGEX = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)

# Input
user_name = input("Enter username: ")
pass_word = getpass.getpass("Enter password: ")

# Validation
if not USERNAME_REGEX.match(user_name):
    print("❌ Invalid username")
    print("Username must be 3–15 characters and contain only letters and numbers.")
    exit()

if not PASSWORD_REGEX.match(pass_word):
    print("❌ Invalid password")
    print(
        "Password must be at least 8 characters long and include:\n"
        "- One uppercase letter\n"
        "- One lowercase letter\n"
        "- One number\n"
        "- One special character (@$!%*?&)"
    )
    exit()

# Mask password
masked_password = "*" * len(pass_word)

print(
    f"✅ Hey {user_name}, your password {masked_password} "
    f"is {len(pass_word)} characters long."
)
