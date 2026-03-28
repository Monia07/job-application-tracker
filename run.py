from application import JobApplication
from storage import load_applications, save_applications


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

        if choice == "1":
            if not applications:
                print("No applications found.")
            else:
                for application in applications:
                    print("\n------------------------------")
                    print(f"ID: {application.id}")
                    print(f"Company: {application.company_name}")
                    print(f"Job Title: {application.job_title}")
                    print(f"Status: {application.status}")
                    print(f"Date Applied: {application.date_applied}")
                    print()
        elif choice == "2":
            company = input("Company name: ")
            title = input("Job title: ")

            new_app = JobApplication(
                id=len(applications) + 1,
                company_name=company,
                job_title=title,
                status="applied",
                date_applied="",
                deadline="",
                contact_name="",
                contact_email="",
                follow_up_date="",
                job_link="",
                notes=""
            )

            applications.append(new_app)
            save_applications(applications)

            print("Application added!")

        elif choice == "0":
            print("\nThank you for using Job Application Tracker!")
            break

        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    main()