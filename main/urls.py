from django.urls import path 
from . import views

app_name= 'main'

urlpatterns = [
    path('profile/<id>',views.home,name='home')
]
