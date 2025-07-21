# form_app/models.py

from django.db import models

class FormResponse(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email_address}"
