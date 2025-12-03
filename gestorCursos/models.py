from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alumnos_creados')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
