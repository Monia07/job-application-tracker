class JobApplication:
    def __init__(
        self,
        id,
        company_name,
        job_title,
        status,
        date_applied,
        deadline=None,
        contact_name=None,
        contact_email=None,
        follow_up_date=None,
        job_link=None,
        notes=None
    ):
        self.id = id
        self.company_name = company_name
        self.job_title = job_title
        self.status = status
        self.date_applied = date_applied
        self.deadline = deadline
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.follow_up_date = follow_up_date
        self.job_link = job_link
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "job_title": self.job_title,
            "status": self.status,
            "date_applied": self.date_applied,
            "deadline": self.deadline,
            "contact_name": self.contact_name,
            "contact_email": self.contact_email,
            "follow_up_date": self.follow_up_date,
            "job_link": self.job_link,
            "notes": self.notes
        }
    

    @staticmethod
    def from_dict(data):
        return JobApplication(
            id=data.get("id"),
            company_name=data.get("company_name"),
            job_title=data.get("job_title"),
            status=data.get("status"),
            date_applied=data.get("date_applied"),
            deadline=data.get("deadline"),
            contact_name=data.get("contact_name"),
            contact_email=data.get("contact_email"),
            follow_up_date=data.get("follow_up_date"),
            job_link=data.get("job_link"),
            notes=data.get("notes"),
        )

    

        