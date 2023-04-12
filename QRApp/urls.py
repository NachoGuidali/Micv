from django.contrib import admin
from django.urls import path, include
from .views import home, cv, login
from django.contrib.auth.views import LoginView 

urlpatterns = [
   
    path('home', home),
    path("cv", cv),
    path("",LoginView.as_view(), name="login")

]