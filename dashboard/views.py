

from django.shortcuts import render
from contacts.models import Contact

def dashboard(request):

    total_contacts = Contact.objects.count()

    contacted = Contact.objects.filter(status="contacted").count()

    interview_planned = Contact.objects.filter(
        status="responded"
    ).count()

    interview_completed = Contact.objects.filter(
        status="done"
    ).count()

    context = {
        "total_contacts": total_contacts,
        "contacted": contacted,
        "interview_planned": interview_planned,
        "interview_completed": interview_completed,
    }

    return render(request, "dashboard/dashboard.html", context)