from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = "__all__"

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(cat.id, cat.get_friendly_name()) for cat in categories]

        self.fields['category'].choices = friendly_names
