
from django.contrib import admin
from django.urls import path , include
from parlour import views


urlpatterns = [
     path('', views.home, name='home'),
     path('services/', views.services, name='services'),
     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
     path('thankyou/<int:id>/', views.thankyou, name='thankyou'),
]
