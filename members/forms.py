from django import forms
from .models import Member


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders to default billing info for member
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_county_or_region': 'County / Region',
            'default_postcode': 'Postcode',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
