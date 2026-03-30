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

            while job_link:
                if job_link.startswith("http://") or job_link.startswith("https://"):
                    break
                else:
                    print("Invalid URL. Please enter a valid link or leave empty.")
                    job_link = input("Job link: ").strip()

            if not job_link:
                job_link = "Not specified"

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
        elif choice == "3":
            search_term = input("Enter company or job title to search: ").strip().lower()

            results = []

            for application in applications:
                if (search_term in application.company_name.lower() or
                    search_term in application.job_title.lower()):
                    results.append(application)

            if results:
                print("\nSearch results:")
                for application in results:
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
            else:
                print("No matching applications found.")                       
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
        elif choice == "6":
            application_id = input("Enter application ID to delete: ").strip()

            found = False

            for application in applications:
                if str(application.id) == application_id:
                    confirm = input("Are you sure you want to delete this application? (y/n): ").strip().lower()

                    if confirm == "y":
                        applications.remove(application)
                        save_applications(applications)
                        print("Application deleted.")
                    else:
                        print("Deletion cancelled.")

                    found = True
                    break

            if not found:
                print("Application not found.")
        elif choice == "7":
            today = input("Enter today's date (YYYY-MM-DD): ").strip()

            upcoming = []
            expired = []

            for application in applications:
                if application.deadline != "Not specified":
                    if application.deadline >= today:
                        upcoming.append(application)
                    else:
                        expired.append(application)

            print("\nUpcoming deadlines:")
            if upcoming:
                for app in upcoming:
                    print("------------------------------")
                    print(f"ID: {app.id}")
                    print(f"Company: {app.company_name}")
                    print(f"Deadline: {app.deadline}")
            else:
                print("No upcoming deadlines.")

            print("\nExpired deadlines:")
            if expired:
                for app in expired:
                    print("------------------------------")
                    print(f"ID: {app.id}")
                    print(f"Company: {app.company_name}")
                    print(f"Deadline: {app.deadline}")
            else:
                print("No expired deadlines.")
        elif choice == "8":
            today = input("Enter today's date (YYYY-MM-DD): ").strip()

            due_followups = []

            for application in applications:
                if application.follow_up_date != "Not specified":
                    if application.follow_up_date <= today:
                        due_followups.append(application)

            print("\nFollow-ups due:")

            if due_followups:
                for app in due_followups:
                    print("\n------------------------------")
                    print(f"ID: {app.id}")
                    print(f"Company: {app.company_name}")
                    print(f"Follow-up Date: {app.follow_up_date}")
                    print(f"Status: {app.status}")
            else:
                print("No follow-ups due.") 
        elif choice == "9":
            with open("report.txt", "w") as file:
                file.write("=== JOB APPLICATION TRACKER REPORT ===\n")
                file.write("Generated automatically\n\n")

                for app in applications:
                    file.write("------------------------------\n")
                    file.write(f"ID: {app.id}\n")
                    file.write(f"Company: {app.company_name}\n")
                    file.write(f"Job Title: {app.job_title}\n")
                    file.write(f"Status: {app.status}\n")
                    file.write(f"Date Applied: {app.date_applied}\n")
                    file.write(f"Deadline: {app.deadline}\n")
                    file.write(f"Contact Name: {app.contact_name}\n")
                    file.write(f"Contact Email: {app.contact_email}\n")
                    file.write(f"Follow-up Date: {app.follow_up_date}\n")
                    file.write(f"Job Link: {app.job_link}\n")
                    file.write(f"Notes: {app.notes}\n\n")

            print("\nReport exported to report.txt")                                               
        elif choice == "0":
            print("\nThank you for using Job Application Tracker!")
            break

        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    main()