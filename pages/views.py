from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class MaizePageView(TemplateView):
    template_name = 'pages/maize.html'

class OnionsPageView(TemplateView):
    template_name = 'pages/onions.html'

class CabbaPageView(TemplateView):
    template_name = 'pages/cabb.html'

class TomatoesPageView(TemplateView):
    template_name = 'pages/tomatoes.html'

class IndvePageView(TemplateView):
    template_name = 'pages/indve.html'

class BusbeansPageView(TemplateView):
    template_name = 'pages/bushbeans.html'

class ClimbbeansPageView(TemplateView):
    template_name = 'pages/climbbeans.html'

class GrassPageView(TemplateView):
    template_name = 'pages/grass.html'

class LegumesPageView(TemplateView):
    template_name = 'pages/legumes.html'

class WatermelonPageView(TemplateView):
    template_name = 'pages/watermelon.html'
