from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Suscriptor
from django.db import IntegrityError
from django.contrib.auth.views import LoginView
from .forms import *


def index(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def suscribir(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                # Verificar si el email ya existe en la base de datos
                if Suscriptor.objects.filter(email=email).exists():
                    # Si el usuario ya está registrado, mostrar un mensaje en pantalla
                    return render(request, 'core/ya_registrado_list.html', {'email': email})
                
                # Si el email no existe en la base de datos, guardarlo
                Suscriptor.objects.create(email=email)
                
                # Redirigir a la página de éxito
                return redirect('core:suscripcion_exitosa_list')
            except IntegrityError:
                # En caso de error, redirigir a la misma página con un mensaje de error
                return render(request, 'core/index.html', {'error': 'Error al procesar la solicitud'})
    # Renderizar el formulario de suscripción en caso de método GET o si ocurrió un error
    return render(request, 'core/index.html')

def suscripcion_exitosa_list(request):
    return render(request, 'core/suscripcion_exitosa_list.html')

def ya_registrado_list(request):
    return render(request, 'core/ya_registrado_list.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
