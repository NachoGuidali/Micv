from django.contrib import admin
from django.urls import path, include
from .views import home, cv

urlpatterns = [
   
    path('', home),
    path("cv", cv)

]