from storage import load_applications


def display_menu():
    print("\n=== Job Application Tracker ===")
    print("1. View all applications")
    print("2. Add application")
    print("3. Search applications")
    print("4. Update application status")
    print("5. Add or edit notes")
    print("6. Delete application")
    print("7. View upcoming / expired deadlines")
    print("8. View follow-ups due")
    print("9. Export report")
    print("0. Exit")


def main():
    applications = load_applications()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("\nThank you for using Job Application Tracker!")
            break
        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    main()