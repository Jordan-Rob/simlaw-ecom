from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(View):
    def get(self, *args, **kwargs):
        form = ContactForm
        context = {
            'form':form,        
        }
        return render(self.request, 'pages/contact.html', context )

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            contact = Contact(
                name = name,
                email = email, 
                phone = phone,
                subject = subject,
                message = message
            )
            contact.save() 
            messages.success(self.request, "Your  Message was succesfully sent")
            return redirect('home')

            
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
