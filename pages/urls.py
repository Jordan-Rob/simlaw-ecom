from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('maize/', MaizePageView.as_view(), name='maize'),
    path('onions/',  OnionsPageView.as_view(), name ='onions'),
    path('cabbage/', CabbaPageView.as_view(), name='cabbage'),
    path('indigenous-vegetables/', IndvePageView.as_view(), name='veg'),
    path('tomatoes/', TomatoesPageView.as_view(), name='tomatoes'),
    path('bush-beans/', BusbeansPageView.as_view(), name='bbeans'),
    path('climbing-beans/', ClimbbeansPageView.as_view(), name='cbeans'),
    path('grass/', GrassPageView.as_view(), name='grass'),
    path('legumes/', LegumesPageView.as_view(), name='legumes'),
    path('watermelon/', WatermelonPageView.as_view(), name='watermelon')
]