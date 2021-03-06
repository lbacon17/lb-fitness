from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your query was submitted successfully')
        else:
            messages.error(request, 'Your query could not be sent')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
