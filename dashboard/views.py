
"""
from django.shortcuts import render
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

@login_required

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

    return render(request, "dashboard/dashboard.html", context)"""

from django.shortcuts import render
from contacts.models import Contact
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    user_contacts = Contact.objects.filter(owner=request.user)

    total_contacts = user_contacts.count()

    contacted = user_contacts.filter(
        status="contacted"
    ).count()

    interview_planned = user_contacts.filter(
        status="responded"
    ).count()

    interview_completed = user_contacts.filter(
        status="done"
    ).count()

    context = {
        "total_contacts": total_contacts,
        "contacted": contacted,
        "interview_planned": interview_planned,
        "interview_completed": interview_completed,
    }

    return render(request, "dashboard/dashboard.html", context)

