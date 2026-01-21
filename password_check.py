import getpass

user_name = input("Enter username - ")
pass_word = getpass.getpass("Enter password - ")

secret_password = len(pass_word) * "*"
print(
    f"Hey {user_name}, your password {secret_password} is {len(pass_word)} characters long."
)
