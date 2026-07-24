from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
