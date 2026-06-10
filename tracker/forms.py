from django import forms
from django.core.exceptions import ValidationError
from datetime import date

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable future dates in the calendar picker
        self.fields["date_applied"].widget.attrs["max"] = date.today().isoformat()

    def clean_date_applied(self):
        date_applied = self.cleaned_data["date_applied"]

        if date_applied > date.today():
            raise ValidationError(
                "Application date cannot be in the future."
            )

        return date_applied