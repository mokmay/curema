from django import forms
from .models import Contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone_number","email","status"]

        widgets = {
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }
