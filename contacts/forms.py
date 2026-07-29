from django import forms
from .models import Contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone_number","email","status"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "contact-form__input",
                "placeholder": "Enter full name",
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "contact-form__input",
                "placeholder": "Enter phone number",
            }),
            "email": forms.EmailInput(attrs={
                "class": "contact-form__input",
                "placeholder": "Enter email address",
            }),
            "status": forms.Select(attrs={
                "class": "contact-form__input",
            }),
        }

