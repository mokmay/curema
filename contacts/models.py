from django.db import models

class Contact(models.Model):
    STATUS_CHOICES = [
        ("not_contacted", "Not Contacted"),
        ("contacted", "Contacted"),
        ("responded", "Responded"),
        ("done", "Done"),
    ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=50, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="not_contacted"
    )

    def __str__(self):
        return self.name
