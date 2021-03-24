from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm
from .models import Contact


def contact(request):
    contact_request = None
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_request = contact_form.save(commit=False)
            contact_request.user = request.user
            contact_request.save()
            messages.success(request, 'Your query was submitted successfully')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Your query could not be sent')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
