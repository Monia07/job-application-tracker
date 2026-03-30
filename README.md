# Job Application Tracker

## Live Project

The live version of this project can be found here: [Job Application Tracker - Live Link](DIN_HEROKU_URL_HÄR)

---

## Introduction

Job Application Tracker is a Python command-line application designed to help users organise and manage job applications efficiently.

The project is based on a real-world need. As I am approaching the end of my studies at Code Institute, I will soon begin applying for roles within full-stack development. This will likely involve managing multiple applications at once, making it difficult to track progress, deadlines, and follow-ups manually.

This application provides a structured and practical solution by allowing users to store and manage job application data in one place through a simple command-line interface.

---

## User Stories

To ensure the application meets the needs of a job seeker, the following goals were defined:

- **As a job seeker**, I want to quickly log new applications so I don't forget where I have applied.
- **As a user**, I want to see a list of upcoming deadlines so I can prioritise my tasks.
- **As a user**, I want to update the status of my applications (e.g., from 'Applied' to 'Interview') to maintain an accurate overview.
- **As a technical user**, I want to work within the terminal to avoid the distractions of a heavy graphical interface.

---

## Rationale

The development of this application was driven by a real and immediate need.

As I approach the end of my studies at Code Institute, I will begin applying for roles within full-stack development. This process typically involves submitting multiple applications across different companies, each with its own deadlines, statuses, and follow-up requirements.

Managing this information manually can quickly become inefficient and error-prone. Important details such as application deadlines, interview dates, or follow-up reminders can easily be overlooked.

This project was designed to provide a structured and centralised way to manage that information in a clear and organised manner.

The application allows users to store, update, and retrieve job application data in one place. By implementing CRUD functionality, users can track their progress, maintain relevant notes, and ensure that important actions such as follow-ups are not missed.

A command-line interface (CLI) was chosen to focus on core programming principles such as data handling, logic flow, and validation, rather than interface design. This supports the goal of building a robust and well-structured backend application.

JSON was used as the data storage method to enable simple, readable, and structured data handling without introducing unnecessary complexity. This allowed the project to focus on implementing functionality and validation effectively.

During development, it became clear that while JSON works well in a local environment, deployment introduces limitations due to Heroku’s ephemeral file system. This highlighted the importance of understanding how different environments affect data persistence.

This project reflects an understanding that different technical choices are appropriate at different stages of development. While JSON is suitable for a functional MVP, more advanced solutions such as PostgreSQL or Google Sheets API could be implemented in future iterations to support persistent storage in a deployed environment.

Overall, the application provides a practical solution to a real-world problem while demonstrating structured programming, data modelling, and awareness of deployment considerations.

---

## Design (M4.1)

_This section documents the logic and flow of the application, meeting the requirements for Merit/Distinction planning._

### Flowchart

The following flowchart illustrates the application's logic, including user navigation, input validation, and data handling loops.

**[INSERT YOUR FLOWCHART IMAGE HERE: ![Flowchart](path/to/your/image.png)]**

---

## Data Model

The application uses a structured data model for each job entry to ensure data integrity:

- **id**: Unique identifier for each entry.
- **company_name**: Name of the hiring company.
- **job_title**: Title of the role applied for.
- **status**: Current status (e.g., Pending, Interview, Rejected, Offer).
- **date_applied**: Date the application was submitted.
- **deadline**: Application or task deadline.
- **contact_name & email**: Recruiter or hiring manager details.
- **notes**: Additional relevant information.

---

## Technologies Used

- **Python 3**: Core programming language.
- **JSON**: Used for data storage and manipulation.
- **[LIST ANY LIBRARIES HERE, e.g., Os, Datetime]**: Used for [EXPLAIN WHY, e.g., handling file paths and date formatting].

---

## Features

- View all applications
- Add new application
- Search applications
- Update application status
- Add and edit notes
- Delete applications
- View deadlines (upcoming & expired)
- View follow-ups
- Export report to file

---

## Testing

### Manual Testing Table (M5.2)

_The following tests were performed to ensure the application is robust and handles invalid data gracefully (Defensive Design)._

| Feature             | Input                             | Expected Result                                     | Outcome  |
| :------------------ | :-------------------------------- | :-------------------------------------------------- | :------- |
| **Main Menu**       | Invalid option (e.g., "99")       | System shows error and prompts for valid choice     | **Pass** |
| **Add Application** | Empty company name                | System rejects input and requires a name            | **Pass** |
| **Date Validation** | Invalid date (e.g., "2024-13-45") | System catches error and asks for YYYY-MM-DD format | **Pass** |
| **Search**          | Company not in records            | System notifies user that no matches were found     | **Pass** |
| **Delete**          | Confirm with "n"                  | Operation is cancelled and no data is removed       | **Pass** |
| **ID Input**        | Non-numeric ID (e.g., "ABC")      | System catches ValueError and asks for a number     | **Pass** |

### Validation (PEP8)

The code has been validated using the **CI Python Linter** to ensure compliance with PEP8 standards.

- **Result**: No significant errors or indentation issues were found.

**[INSERT SCREENSHOT OF YOUR LINT REPORT HERE]**

---

## Deployment (LO9)

The application was deployed using **Heroku**.

### Deployment Steps:

1. Create a `requirements.txt` file using `pip freeze > requirements.txt`.
2. Create a `Procfile` with the content: `python: python3 run.py`.
3. Create a new app on the Heroku Dashboard.
4. Connect the GitHub repository and select the main branch for deployment.
5. Add the `heroku/python` buildpack under Settings.

### Persistence Note:

It is important to note that Heroku uses an **ephemeral file system**. This means that data saved to the JSON file during a session will be reset when the Heroku dyno restarts. This is a known limitation of the current MVP version.

---

## Version Control

- **Git** was used throughout development for version control.
- Frequent commits were made with clear, descriptive messages to document the progress of features and bug fixes.

---

## Known Bugs & Limitations

- Data resets on Heroku due to the ephemeral file system.
- CLI environment limitations for displaying large data tables.

---

## Future Improvements

- **Google Sheets API**: To provide persistent cloud storage.
- **PostgreSQL**: To implement a full relational database.
- **Improved UI**: Using libraries like 'Rich' for better terminal visuals.

---

## Credits

- **Code Institute**: For the project framework and learning materials.
- **Python Documentation**: For technical guidance on JSON and Datetime modules.

---

## Author

[Monia]
