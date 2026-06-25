def is_valid_username(username):
    if len(username) >= 4 and len(username) <= 16 and " " not in username:
        return True
    else:
        return False
def get_password_strength(password):
    if len(password) < 8:
        return "WEAK"
    elif len(password) >= 8 and len(password) <= 11:
        return "MEDIUM"
    else:
        return "STRONG"
def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False
def create_account(username, password):
    username_valid = is_valid_username(username)
    password_valid = is_valid_password(password)
    password_strength = get_password_strength(password)
    if username_valid and password_valid:
        print(f"""
Account created successfully!
Username: {username}
Password Strength: {password_strength}
""")
    elif not username_valid: #unreachable code when made into a while loop
        print("Account creation failed. Please input a valid username.")
    else: #unreachable code when made into a while loop
        print("Account creation failed. Please input a valid password.")


username = ""
password = ""

while not is_valid_username(username):
    username = input("Enter your username: ")
    if not is_valid_username(username):
        print("This is not a valid username. Please try again: ")
while not is_valid_password(password):    
    password = input("Enter your password: ")
    if not is_valid_password(password):
        print("This is not a valid password. Please try again: ")

create_account(username, password)
