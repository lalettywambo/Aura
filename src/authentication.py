from src.models import User
from src.data_manager import save_user, get_users


def register_user():
    print("\n Create Your AURA Account ")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")

    user = User(name, email, password)

    save_user(user)

    return user


def login_user():
    print("\n AURA Login")

    email = input("Enter your email: ")
    password = input("Enter your password:")

    users = get_users()

    for user in users:
        if user["email"] == email:
            print(f"\n Welcome back, {user['name']}!")
            return user

    print("\n❌ Incorrect email or password.")
    return None