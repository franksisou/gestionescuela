from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FormularioRegistro
from .models import Perfil

def pagina_principal(request):
    """Vista para la página principal pública (landing page)"""
    return render(request, 'landing.html')

def vista_login(request):
    if request.method == "POST":
        nombre_usuario = request.POST.get("username")
        contrasena = request.POST.get("password")

        usuario = authenticate(request, username=nombre_usuario, password=contrasena)
        if usuario:
            login(request, usuario)
            return redirect('Inicio')  # Redirige al dashboard en /inicio/
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'login.html')


def vista_logout(request):
    logout(request)
    return redirect('landing')  # Redirige a la página principal pública


def vista_registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            # El perfil ya fue creado por el signal, solo actualizamos el rol si es necesario
            rol = formulario.cleaned_data.get('rol', 'usuario')
            perfil = Perfil.objects.get(usuario=usuario)
            perfil.rol = rol
            perfil.save()
            return redirect('login')
    else:
        formulario = FormularioRegistro()

    return render(request, 'registro.html', {'form': formulario})



