from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
    full_names = models.CharField(max_length=350)
    phone = models.IntegerField() 
    address = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('user_dash', args=[str(self.id)])


