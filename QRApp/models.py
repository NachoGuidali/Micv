from django.db import models
from django.utils import timezone

# Create your models here.
class Qrlink(models.Model):
    qr = models.ImageField()
    titulo = models.CharField(max_length=100)
