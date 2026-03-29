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
                    print(f"Deadline: {application.deadline}")
                    print(f"Contact Name: {application.contact_name}")
                    print(f"Contact Email: {application.contact_email}")
                    print(f"Follow-up Date: {application.follow_up_date}")
                    print(f"Job Link: {application.job_link}")
                    print(f"Notes: {application.notes}")
                    print()
        elif choice == "2":
            company = input("Company name: ").strip()
            title = input("Job title: ").strip()
            date_applied = input("Date applied (YYYY-MM-DD): ").strip()
            deadline = input("Deadline (YYYY-MM-DD): ").strip()
            contact_name = input("Contact name: ").strip()
            contact_email = input("Contact email: ").strip()
            follow_up_date = input("Follow-up date (YYYY-MM-DD): ").strip()
            job_link = input("Job link: ").strip()

            new_app = JobApplication(
                id=len(applications) + 1,
                company_name=company,
                job_title=title,
                status="applied",
                date_applied=date_applied if date_applied else "Not specified",
                deadline=deadline if deadline else "Not specified",
                contact_name=contact_name if contact_name else "Not specified",
                contact_email=contact_email if contact_email else "Not specified",
                follow_up_date=follow_up_date if follow_up_date else "Not specified",
                job_link=job_link if job_link else "Not specified",
                notes="Not specified"
            )

            applications.append(new_app)
            save_applications(applications)

            print("Application added!")
        elif choice == "4":
            application_id = input("Enter application ID: ").strip()
            new_status = input(
                "Enter new status (applied/interview/offer/rejected/withdrawn): "
            ).strip().lower()

            found = False

            for application in applications:
                if str(application.id) == application_id:
                    application.status = new_status
                    found = True
                    save_applications(applications)
                    print("Application status updated!")
                    break

            if not found:
                print("Application not found.")
        elif choice == "5":
            application_id = input("Enter application ID: ").strip()
            notes = input("Enter notes: ").strip()

            found = False

            for application in applications:
                if str(application.id) == application_id:
                    application.notes = notes
                    found = True
                    save_applications(applications)
                    print("Notes updated!")
                    break

            if not found:
                print("Application not found.")
                
        elif choice == "0":
            print("\nThank you for using Job Application Tracker!")
            break

        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    main()