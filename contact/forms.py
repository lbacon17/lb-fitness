from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email_address', 'subject', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email_address': 'E-mail Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False