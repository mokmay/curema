from django.test import TestCase
from django.urls import reverse
from .models import Contact


class ContactViewTests(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name="John",
            phone_number="07123456789",
            email="john@example.com",
            status="P"
        )

    def test_read_view(self):
        response = self.client.get(reverse("read"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")

    def test_create_view(self):
        response = self.client.post(
            reverse("create"),
            {
                "name": "Jane",
                "phone_number": "07987654321",
                "email": "jane@example.com",
                "status": "P",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 2)

    def test_edit_view(self):
        response = self.client.post(
            reverse("edit", args=[self.contact.id]),
            {
                "name": "Johnny",
                "phone_number": "07000000000",
                "email": "johnny@example.com",
                "status": "Y",
            }
        )

        self.contact.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.contact.name, "Johnny")
        self.assertEqual(self.contact.email, "johnny@example.com")
        self.assertEqual(self.contact.status, "Y")

    def test_delete_view(self):
        response = self.client.post(
            reverse("delete", args=[self.contact.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 0)
