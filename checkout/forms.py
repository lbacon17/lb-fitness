from django import forms
from .models import ShopOrder


class ShopOrderForm(forms.ModelForm):
    class Meta:
        model = ShopOrder
        fields = ('full_name', 'email_address', 'phone_number',
                  'address_line1', 'address_line2', 'town_or_city',
                  'county_or_region', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'county_or_region': 'County or Region',
            'postcode': 'Postcode',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
