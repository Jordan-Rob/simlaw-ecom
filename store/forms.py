from django import forms
from django.forms import ModelForm
from .models import *

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = [ 'delivery_option' ]