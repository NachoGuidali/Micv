from django.shortcuts import render
from .models import Qrlink

# Create your views here.
def home(request):
    context = {
        "links" : Qrlink.objects.all()
    }
    return render(request, "index.html", context=context )