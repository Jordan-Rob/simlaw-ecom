from django import forms
from django.forms import ModelForm
from .models import *

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = [ 'delivery_option' ]

class CheckoutForm(forms.Form):
    phone = forms.CharField()
    location = forms.CharField()
    address = forms.CharField()
    building_apartment_name = forms.CharField(required=False)
    order_notes = forms.CharField( required=False )        