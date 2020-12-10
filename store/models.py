from django.db import models
from django.urls import reverse
from users.models import CustomUser 
from model_utils import Choices

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name    

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    sku = models.IntegerField()
    image_570x679 = models.ImageField(upload_to='pdt_imgs/detail')
    image_115x122 = models.ImageField(upload_to='pdt_imgs/cart')
    image_270x293 = models.ImageField(upload_to='pdt_imgs/listin')
    #available = models.BooleanField(default=True)
    #discount = models.IntegerField(default = 0)
    description = models.CharField(max_length=120, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('pdt_detail', args=[str(self.id)])

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', args= [str(self.id)] )    

class Order(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    billing_details = models.ForeignKey( 'BillingDetails', on_delete = models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey( 'Payment', on_delete = models.SET_NULL, blank=True, null=True)
    delivery = models.ForeignKey( 'Delivery', on_delete = models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.customer.username

    def total_price(self):
        total = 0
        for orderitem in self.orderitem_set.all():
            total += orderitem.get_final_price()
        return total   

    def total_price_deliv(self):
        total = self.total_price() + 5000
        return total

    def total_price_deliv_pickup(self):
        total = self.total_price() + 2000
        return total         

class OrderItem(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)    
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} "

    def  get_total_item_price(self):
        return self.quantity * self.product.price
    '''
    def get_total_item_discount_price(self):
        discount_price = self.product.price - (self.product.discount/100 * self.product.price)      
        return self.quantity * discount_price
    '''
    def get_final_price(self):
        '''
        if self.product.discount > 0:
            return self.get_total_item_discount_price()
        '''    
        return  self.get_total_item_price()


class Delivery(models.Model):
    STATUS = Choices(
        ('doorstep', ('delivery to doorstep')),
        ('pickup', ('delivery to pick up point')),
    )
   # [..]
    delivery_option = models.CharField(
       max_length=32,
       choices=STATUS,
       default=STATUS.doorstep,
    )           

class BillingDetails(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    building_apartment_name = models.CharField(max_length=200, null=True, blank=True)
    order_notes = models.CharField( max_length=300, null=True, blank=True )  

    def __str__(self):
        return self.customer.username


class Payment(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    pay_on_delivery = models.BooleanField(default=False , null=True, blank=True)  
    complete = models.BooleanField(default=False , null=True, blank=True)  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username

class Pickup(models.Model):
    pickup_location = models.CharField(max_length=122)
    active = models.BooleanField(default=False)  

    def __str__(self):
        return self.pickup_location 
        