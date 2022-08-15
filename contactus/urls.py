from django.urls import path 
from . import views


urlpatterns = [
    path('form/',views.ContactUsView,name='contactus')
]