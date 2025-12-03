"""
URL configuration for escuelaChuckyAlan_Luis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestorCursos.views import (
    indice,
    lista_cursos,
    crear_curso,
    actualizar_curso,
    eliminar_curso,
    lista_alumnos,
    crear_alumno,
    actualizar_alumno,
    eliminar_alumno,
)
from gestorUser.views import vista_login, vista_logout, vista_registro, pagina_principal

urlpatterns = [

    # ADMIN
    path('admin/', admin.site.urls),

    # PÁGINA PRINCIPAL PÚBLICA (Landing Page)
    path('', pagina_principal, name='landing'),

    # DASHBOARD - Requiere login
    path('inicio/', indice, name='Inicio'),

    # CURSOS
    path('Cursos/', lista_cursos, name='cursos_list'),
    path('CrearCurso/', crear_curso, name='curso_create'),
    path('EditarCurso/<int:id>/', actualizar_curso, name='curso_update'),
    path('EliminarCurso/<int:id>/', eliminar_curso, name='curso_delete'),

    # ALUMNOS
    path('Alumnos/', lista_alumnos, name='alumnos_list'),
    path('CrearAlumno/', crear_alumno, name='alumno_create'),
    path('EditarAlumno/<int:id>/', actualizar_alumno, name='alumno_update'),
    path('EliminarAlumno/<int:id>/', eliminar_alumno, name='alumno_delete'),

    # USUARIOS (GESTORUSER)
    path('Login/', vista_login, name='login'),
    path('Logout/', vista_logout, name='logout'),
    path('Registro/', vista_registro, name='registro'),
]

