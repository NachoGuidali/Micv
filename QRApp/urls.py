from django.contrib import admin
from django.urls import path
from .views import home, cv, login_view, register_view, logout_view, QrNuevo, generar_qr
from django.contrib.auth.views import LoginView 

urlpatterns = [
   
    path('home', home, name="home"),
    
    path("cv", cv),
    path("", login_view, name="login"),
    path("register", register_view, name="register"),
    path("logout", logout_view, name="logout"),
    path("qrnuevo", QrNuevo, name="QrNuevo"),
    path("generarqr", generar_qr, name="generarqr"),
]
