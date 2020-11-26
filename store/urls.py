from django.urls import path
from .views import *

urlpatterns = [
    path('', Pdt_listin.as_view(), name='listin'),
    path('product/<int:pk>/', Pdt_detail.as_view(), name='pdt_detail')

]