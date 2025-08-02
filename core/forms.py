from django import forms
from .models import AddToCartForm, ContactForm

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = AddToCartForm
        fields = ['quantity', 'product_id']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('__all__')


