from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.decorators import login_required

@login_required

def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            if form.is_valid():
                contact = form.save(commit=False)
                contact.owner = request.user
                contact.save()
            return redirect("read")
        else:
            return redirect("sorry not sorry")
    else:
        form = ContactForm()

    return render(request, "contacts/contact_form.html", {"form": form})

def read(request):
    contacts = Contact.objects.filter(owner=request.user)

    return render(request, "contacts/read.html", {
        "contacts": contacts
    })

def delete(request, id):

    contact = get_object_or_404(
        Contact,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        contact.delete()
        return redirect("read")

    return render(request, "contacts/delete.html", {
        "contact": contact
    })

def edit(request, id):
    contact = get_object_or_404(
        Contact,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect("read")
    else:
        form = ContactForm(instance=contact)

    return render(request, "contacts/contact_form.html", {
        "form": form
    })

def details(request, pk):

    contact = get_object_or_404(
        Contact,
        pk=pk,
        owner=request.user
    )
    return render(request, "contacts/details.html", {
        "contact": contact
    })