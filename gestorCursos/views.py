from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Curso, Alumno
from .forms import FormularioCurso, FormularioAlumno

# ============================
#       INICIO
# ============================

@login_required
def indice(request):
    # Estadísticas generales
    total_cursos = Curso.objects.count()
    total_alumnos = Alumno.objects.count()
    
    if request.user.is_superuser:
        mis_alumnos = total_alumnos
    else:
        mis_alumnos = Alumno.objects.filter(creador=request.user).count()
    
    # Cursos con más alumnos
    cursos_populares = Curso.objects.all()[:5]
    cursos_data = []
    for curso in cursos_populares:
        cantidad = Alumno.objects.filter(curso=curso).count()
        porcentaje = round((cantidad / total_alumnos * 100), 1) if total_alumnos > 0 else 0
        cursos_data.append({
            'curso': curso.nombre,
            'cantidad': cantidad,
            'porcentaje': porcentaje
        })
    
    contexto = {
        'total_cursos': total_cursos,
        'total_alumnos': total_alumnos,
        'mis_alumnos': mis_alumnos,
        'cursos_data': cursos_data,
    }
    
    return render(request, 'index.html', contexto)


# ============================
#       CURSOS
# ============================

@login_required
def lista_cursos(request):
    # Solo superusuarios pueden acceder
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para gestionar cursos.')
        return redirect('Inicio')
    
    cursos = Curso.objects.all()
    
    # Estadísticas para cada curso
    cursos_con_estadisticas = []
    for curso in cursos:
        total_estudiantes = Alumno.objects.filter(curso=curso).count()
        cursos_con_estadisticas.append({
            'curso': curso,
            'total_estudiantes': total_estudiantes
        })
    
    # Estadísticas generales
    total_cursos = cursos.count()
    total_estudiantes = Alumno.objects.count()
    promedio_estudiantes = total_estudiantes // total_cursos if total_cursos > 0 else 0
    
    return render(request, 'cursos/list.html', {
        'cursos_con_estadisticas': cursos_con_estadisticas,
        'total_cursos': total_cursos,
        'total_estudiantes': total_estudiantes,
        'promedio_estudiantes': promedio_estudiantes
    })


@login_required
def crear_curso(request):
    # Solo superusuarios pueden crear cursos
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para crear cursos.')
        return redirect('Inicio')
    
    if request.method == 'POST':
        formulario = FormularioCurso(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Curso creado exitosamente.')
            return redirect('cursos_list')
    else:
        formulario = FormularioCurso()
    return render(request, 'cursos/form.html', {'form': formulario})


@login_required
def actualizar_curso(request, id):
    # Solo superusuarios pueden actualizar cursos
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para editar cursos.')
        return redirect('Inicio')
    
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        formulario = FormularioCurso(request.POST, instance=curso)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Curso actualizado exitosamente.')
            return redirect('cursos_list')
    else:
        formulario = FormularioCurso(instance=curso)
    return render(request, 'cursos/form.html', {'form': formulario})


@login_required
def eliminar_curso(request, id):
    # Solo superusuarios pueden eliminar cursos
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para eliminar cursos.')
        return redirect('Inicio')
    
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado exitosamente.')
        return redirect('cursos_list')
    return render(request, 'cursos/delete.html', {'curso': curso})


# ============================
#       ALUMNOS
# ============================

@login_required
def lista_alumnos(request):
    # Todos los usuarios ven todos los alumnos
    alumnos = Alumno.objects.all()
    
    # Estadísticas
    total_alumnos = alumnos.count()
    cursos_activos = Curso.objects.filter(alumno__in=alumnos).distinct().count()
    alumnos_por_curso = {}
    for curso in Curso.objects.all():
        count = alumnos.filter(curso=curso).count()
        if count > 0:
            alumnos_por_curso[curso.nombre] = count
    
    return render(request, 'alumnos/list.html', {
        'alumnos': alumnos,
        'total_alumnos': total_alumnos,
        'cursos_activos': cursos_activos,
        'alumnos_por_curso': alumnos_por_curso
    })


@login_required
def crear_alumno(request):
    if request.method == 'POST':
        formulario = FormularioAlumno(request.POST)
        if formulario.is_valid():
            alumno = formulario.save(commit=False)
            alumno.creador = request.user  # Asignar el creador
            alumno.save()
            messages.success(request, 'Alumno creado exitosamente.')
            return redirect('alumnos_list')
    else:
        formulario = FormularioAlumno()
    
    # Verificar si hay cursos disponibles
    cantidad_cursos = Curso.objects.count()
    
    return render(request, 'alumnos/form.html', {
        'form': formulario,
        'cursos_count': cantidad_cursos
    })


@login_required
def actualizar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    
    # Verificar permisos: superuser o creador del alumno
    if not request.user.is_superuser and alumno.creador != request.user:
        messages.error(request, 'No tienes permisos para editar este alumno.')
        return redirect('alumnos_list')
    
    if request.method == 'POST':
        formulario = FormularioAlumno(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Alumno actualizado exitosamente.')
            return redirect('alumnos_list')
    else:
        formulario = FormularioAlumno(instance=alumno)
    
    cantidad_cursos = Curso.objects.count()
    
    return render(request, 'alumnos/form.html', {
        'form': formulario,
        'cursos_count': cantidad_cursos
    })


@login_required
def eliminar_alumno(request, id):
    # Solo superusuarios pueden eliminar alumnos
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para eliminar alumnos.')
        return redirect('alumnos_list')
    
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        messages.success(request, 'Alumno eliminado exitosamente.')
        return redirect('alumnos_list')
    return render(request, 'alumnos/delete.html', {'alumno': alumno})
