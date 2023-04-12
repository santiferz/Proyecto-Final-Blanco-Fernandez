from django.contrib import admin
from django.urls import path, include 
from core.views import inicio, FormularioFutbol, editar_futbol, eliminar_futbol, agregar_futbol
from django.contrib.auth.views import LogoutView
from core import views

urlpatterns = [
    path("", inicio, name="index"),
    path("mostrar_futbol/", FormularioFutbol, name="mostrar_futbol"),
    path("agregar_futbol/", agregar_futbol, name="agregar_futbol"),
    path("editar_futbol/<int:id_futbol>", editar_futbol, name="editar_futbol"),
    path("eliminar_futbol/<int:id_futbol>", eliminar_futbol, name="eliminar_futbol"),
    path("login", views.login_request, name= "login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="core/logout.html"), name= "Logout"),
    path("leerfutbol", views.leerFutbol, name="leerpersona"),
]