from django.shortcuts import render
from core.models import Futbol
from core.forms import FutbolForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request, "core/base.html")

def FormularioFutbol(request):
    futbol = Futbol.objects.all()
    return render(request, "core/FormularioFutbol.html",{"futbol": futbol})

def agregar_futbol(request):
    if request.method == "POST": 
        futbol_form = FutbolForm(request.POST)
        if futbol_form.is_valid():
            data = futbol_form.cleaned_data
            futbol = Futbol(nombre=data["nombre"], nro_equipos=data["integrantes_equipo"])
            futbol.save()
            return render(request, "core/base.html")
    futbol_form = FutbolForm()    
    return render(request, "core/agregar_futbol.html", {"form": futbol_form})

def editar_futbol(request, id_futbol):
    futbol = Futbol.objects.get(id=id_futbol)
    if request.method == "POST":
        futbol_form = FutbolForm(request.POST)
        if futbol_form.is_valid():
            data = futbol_form.cleaned_data
            futbol.nombre = data["nombre"]
            futbol.nro_equipos = data["Integrantes_del_equipo"]
            futbol.save()
            return render(request, "core/index.html")
    return render(request, "core/editar_futbol.html")

def eliminar_futbol(request, id_futbol):

    futbol = Futbol.objects.get(id=id_futbol)
    name = futbol.nombre
    futbol.delete() 
    return render(request, "core/eliminar_futbol.html", {"nombre_eliminado": name})

def leerFutbol(request):
    futbol = Futbol.objects.all()
    contexto = {"futbol":futbol}
    return render(request, "core/leerfutbol.html", contexto )



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contraseña)

            if user is not None:
                login(request,user)

                return render(request,"core/base.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"core/base.html",{"mensaje":"Datos incorrectos"})
        else:
                return render(request,"core/base.html",{"mensaje":"Formulario erroneo"})
        
    form = AuthenticationForm()
    return render(request,"core/login.html",{'form':form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"core/base.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request,"core/register.html",{"form":form})