from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "company_name",
            "job_title",
            "status",
            "date_applied",
            "deadline",
            "follow_up_date",
            "contact_email",
            "job_link",
            "notes",
        ]
        widgets = {
            "date_applied": forms.DateInput(attrs={"type": "date"}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "follow_up_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4}),
        }