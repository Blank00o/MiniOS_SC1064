users = {
    "myr": "myr123",
    "john": "john123",
    "lyle": "lyle123",
    "user": "password123"
}

current_user = None


def login():
    global current_user

    print("=" * 40)
    print("          MINIOS LOGIN")
    print("=" * 40)

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        current_user = username
        print(f"\nLogin successful!")
        print(f"Welcome, {username}!")
        return True

    print("Invalid username or password.")
    return False


def whoami():
    print(f"Current User: {current_user}")