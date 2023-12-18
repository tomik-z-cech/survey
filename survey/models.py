# survey/models.py
from django.db import models

class SurveyResponse(models.Model):
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    description = models.TextField()
    read = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.name}'s response"