import bcrypt

def register_user(users_db):
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try again.")
        return
    password = input("Enter a password: ")
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users_db[username] = hashed
    print("User registered successfully!")
def login_user(users_db):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db:
        stored_hash = users_db[username]
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            print("Login successful! Welcome,", username)
            return
    print("Invalid username or password. Please try again.")
def main():
    users_db = {}
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user(users_db)
        elif choice == "2":
            login_user(users_db)
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
