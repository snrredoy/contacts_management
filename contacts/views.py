from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


# List contacts (homepage)
def contact_list(request):
    contacts = Contact.objects.all()
    query = request.GET.get("q")
    if query:
        contacts = contacts.filter(first_name__icontains=query) | contacts.filter(
            email__icontains=query
        )
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


# Add contact
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form})


# Edit contact
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {"form": form})


# Delete contact
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/contact_delete.html", {"contact": contact})


# View contact details
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/contact_details.html", {"contact": contact})
