from django.db import models

# Create your models here.
class Qrlink(models.Model):
    qr = models.ImageField()
