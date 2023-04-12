from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Qrlink

# Create your views here.
def home(request):
    context = {
        "links" : Qrlink.objects.all()
    }
    return render(request, "index.html", context=context )

def cv(request):
    return render(request, "cv.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #ahora verificamos si el ussuario y contraseña existe y luego entra a la url
        user = authenticate(request, username=username, password=password)
        contraseña = authenticate(request, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            #si el ususario o contraseña son incorrectos, recarga la pagina con un mensaje de error
            error_message = "Usuario o Contraseña incorrecta"
            return render(request, "registration/login.html", {'error_message' : error_message})

       
    return render(request, "registration/login.html", {})

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("/home")
    
    return render(request, "registration/register.html", {})


"""else:
            #si no existe lo crea y despues entra a la url
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("/home")"""