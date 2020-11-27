from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import CustomUser

class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
