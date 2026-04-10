from django.db import models

from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
        ("withdrawn", "Withdrawn"),
    ]

    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="applied",
    )
    date_applied = models.DateField()
    deadline = models.DateField(blank=True, null=True)
    follow_up_date = models.DateField(blank=True, null=True)
    contact_email = models.EmailField(blank=True)
    job_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
