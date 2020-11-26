from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import *
# Create your views here.

class Pdt_listin(ListView):
    model = Product
    template_name = 'store/shop.html'

class Pdt_detail(DetailView):
    model = Product
    template_name = 'store/product.html'

