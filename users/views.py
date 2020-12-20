from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import CustomUser
from store.models import Order
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')


class UserDashBoardView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'phone', 'address']
    template_name = 'user/user_dashboard.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your Information was succesfully updated")
        return redirect('user_dash', pk=self.request.user.pk)



class UserDashBoardOrdersView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user/user_dash_orders.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(UserDashBoardOrdersView, self).get_context_data( **kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user)
        #order = Order.objects.get(customer=self.request.user)
        #context['orderitems'] = order.orderitem_set.all()
        return context
