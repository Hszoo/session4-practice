from django.contrib import admin
from django.urls import path, include
from carts import views

urlpatterns = [
    path('', views.carthome, name='carthome'),
]
