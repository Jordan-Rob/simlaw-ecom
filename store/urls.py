from django.urls import path
from .views import *

urlpatterns = [
    path('', Pdt_listin.as_view(), name='listin'),
    path('product/<int:pk>/', Pdt_detail.as_view(), name='pdt_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<int:pk>/', remove_item_from_cart, name='remove-item-from-cart'),

]