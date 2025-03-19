from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['phone', 'address', 'postal_code']