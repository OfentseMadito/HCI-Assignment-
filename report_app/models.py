# report_app/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

STATUS_CHOICES = [
    ('reported', 'Reported'),
    ('in_progress', 'In Progress'),
    ('resolved', 'Resolved'),
]

CATEGORY_CHOICES = [
    ('water_leak', 'Water Leak'),
    ('pothole', 'Pothole'),
    ('electricity', 'Electricity'),
    ('illegal_dumping', 'Illegal Dumping'),
    ('streetlight', 'Streetlight'),
    ('sewer_issue', 'Sewer Issue'),
]

class Report(models.Model):
    reference_number = models.CharField(max_length=20, unique=True, editable=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')
    reported_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional for anonymous

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = "RPT-" + str(uuid.uuid4().hex)[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.get_category_display()}"