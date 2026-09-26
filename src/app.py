from src.authentication import register_user, login_user


def start_aura():
    print(" Welcome to AURA ")
    print("Your personal experience starts here.\n")

    print("1. Create an account")
    print("2. Login")

    choice = input("\nChoose an option: ")

    if choice == "1":
        user = register_user()

        print("\n Account Created Successfully ")
        user.display_profile()

    elif choice == "2":
        user = login_user()

        if user:
            print("\nYou are now inside AURA. ")

    else:
        print("\n❌ Invalid choice.")