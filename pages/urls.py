from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]