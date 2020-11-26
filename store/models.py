from django.db import models
from django.urls import reverse

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



        