from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import DeliveryForm, CheckoutForm, PaymentForm

from django.contrib import messages
# Create your views here.

class Pdt_listin(ListView):
    model = Product
    template_name = 'store/shop.html'

class Pdt_detail(DetailView):
    model = Product
    template_name = 'store/product.html'


class CartView( LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            
            order = Order.objects.get(customer=self.request.user, complete=False)
            form = DeliveryForm
            context = {
                'object': order,
                'form': form,
            }
            
            return render(self.request, 'store/cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
    
    
    def post(self, *args, **kwargs):
        form = DeliveryForm(self.request.POST or None)
        order = Order.objects.get(customer=self.request.user, complete=False)   
        if form.is_valid():
            option = form.cleaned_data.get('delivery_option')
            delivery_option = Delivery(
                delivery_option = option,
            )
            delivery_option.save() 
            order.delivery = delivery_option
            order.save()
            return redirect('checkout')  
    

#Function to handle adding items to cart or 
# updating quantity of item incase it's already a cart item     

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk) 
    orderitem, created = OrderItem.objects.get_or_create(
        product=product, customer=request.user, complete=False)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem.quantity +=1
            orderitem.save()
            messages.info(request , "This product quantity was updated in your cart")
            return redirect('cart') 
        else:
            order.orderitem_set.add(orderitem)    
            messages.info(request , "This product was added to your cart")
            return redirect('cart') 
    else:
        order = Order.objects.create(customer=request.user)
        order.orderitem_set.add(orderitem)
        messages.info(request , "This product was added to your cart")
        return redirect('cart' )  


#function to handle removal of item from cart
@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem = OrderItem.objects.filter(
            product=product, customer=request.user, complete=False)[0]
            order.orderitem_set.remove(orderitem)
            messages.info(request , "This product was removed from your cart")
            return redirect('cart' )
        else:
            messages.info(request , "This product was not in your cart")
            return redirect('pdt_detail', pk =pk ) 
    else:
        messages.info(request , "You do not have an active order")
        return redirect('pdt_detail', pk =pk )
   

@login_required
def remove_item_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem = OrderItem.objects.filter(
            product=product, customer=request.user, complete=False)[0]
            if orderitem.quantity > 1:
                orderitem.quantity -=1
                orderitem.save()
            else:
                order.orderitem_set.remove(orderitem)
            messages.info(request , "This product quantity was updated ")
            return redirect('cart' )
        else:
            messages.info(request , "This product was not in your cart")
            return redirect('pdt_detail', pk =pk ) 
    else:
        messages.info(request , "You do not have an active order")
        return redirect('pdt_detail', pk =pk )



class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm
        order = Order.objects.get(customer=self.request.user, complete=False)
        if order.delivery.delivery_option == order.delivery.STATUS.doorstep:
            delivery = order.delivery
            amount = order.total_price()
            amnt = 5000
            text = 'Doorstep Delivery around Kampala'
            total = order.total_price_deliv()
            context = {
                'order':order,
                'amount':amount,
                'delivery': delivery,
                'amnt': amnt,
                'text': text,
                'total': total,
                'form':form
            }
            return render(self.request, 'store/checkout.html', context )
        else:
            delivery = order.delivery
            amount = order.total_price()
            amnt = 2000
            text = 'Delivery at pick up point'
            total = order.total_price_deliv_pickup()
            context = {
                'order':order,
                'amount':amount,
                'delivery': delivery,
                'amnt': amnt,
                'text': text,
                'total': total,
                'form':form
            }
            return render(self.request, 'checkout.html', context )


    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(customer=self.request.user, complete=False)      
            if form.is_valid():
                phone = form.cleaned_data.get('phone')
                location = form.cleaned_data.get('location')
                address = form.cleaned_data.get('address')
                building_apartment_name = form.cleaned_data.get('building_apartment_name ')
                order_notes = form.cleaned_data.get('order_notes')
                billing_details = BillingDetails(
                    customer = self.request.user,
                    phone = phone,
                    location = location,
                    address = address,
                    building_apartment_name = building_apartment_name, 
                    order_notes = order_notes
                )
                billing_details.save() 
                order.billing_details = billing_details
                order.save()
                """
                payment = PaymentTypeModel(
                    description=self.request.user,
                    amount= order.total_price(),
                    currency='UGX',
                    pay_button_text='pay now',
                )
                payment.save()
                """
                return redirect('payment')    
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("cart")


class PaymentView(View):
    def get(self, *args, **kwargs):
        """
        payment = PaymentTypeModel.objects.filter(
            description=self.request.user
        ).first()
        """
        order = Order.objects.get(customer=self.request.user, complete=False)
        form = PaymentForm
        if order.delivery.delivery_option == order.delivery.STATUS.doorstep:
            delivery = order.delivery
            amount = order.total_price()
            amnt = 5000
            text = 'Doorstep Delivery around Kampala'
            total = order.total_price_deliv()
            context = {
                'order':order,
                'amount':amount,
                'delivery': delivery,
                'amnt': amnt,
                'text': text,
                'total': total,
                'form': form,
            }
        
            return render(self.request, 'store/payment.html', context )

        else:
            delivery = order.delivery
            amount = order.total_price()
            amnt = 2000
            text = 'Delivery at pick up point'
            total = order.total_price_deliv_pickup()
            pickup = Pickup.objects.get(active=True)
            context = {
                'order':order,
                'amount':amount,
                'delivery': delivery,
                'amnt': amnt,
                'text': text,
                'total': total,
                'pickup': pickup,
                'form': form,
            }
        
            return render(self.request, 'store/payment.html', context )


    def post(self, *args, **kwargs):
        order = Order.objects.get(customer=self.request.user, complete=False)
        amount = order.total_price()
        form = PaymentForm(self.request.POST or None)
        if form.is_valid():
            pay_on_delivery = form.cleaned_data.get('pay_on_delivery')
            payment = Payment(
                customer=self.request.user,
                amount=amount,
                pay_on_delivery=pay_on_delivery
            )

            payment.save()

            #assign payment to order
            
            order_items = order.orderitem_set.all()
            order_items.update(complete=True)
            for item in order_items:
                item.save()
        
            order.complete = True
            order.payment = payment
            order.save()

            messages.success(self.request, "Your order was succesful")
            return redirect('home')
