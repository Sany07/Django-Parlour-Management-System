
from django.contrib import admin
from django.urls import path , include
from adminsection import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
