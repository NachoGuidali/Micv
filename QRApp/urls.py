from django.contrib import admin
from django.urls import path, include
from .views import home, cv, login_view, register_view, logout_view
from django.contrib.auth.views import LoginView 

urlpatterns = [
   
    path('home', home),
    
    path("cv", cv),
    path("", login_view, name="login"),
    path("register", register_view, name="register"),
    path("logout", logout_view, name="logout")
]