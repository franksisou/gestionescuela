from django import forms
from .models import Curso, Alumno
import re

class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'descripcion']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: PROG101'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del curso'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción del curso'}),
        }
        labels = {
            'codigo': 'Código del Curso',
            'nombre': 'Nombre del Curso',
            'descripcion': 'Descripción',
        }


class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'rut', 'fecha_nacimiento', 'curso']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12.345.678-9'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'curso': 'Curso',
        }
        help_texts = {
            'curso': 'Seleccione el curso al que pertenece el alumno',
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            raise forms.ValidationError('El nombre solo puede contener letras y espacios.')
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', apellido):
            raise forms.ValidationError('El apellido solo puede contener letras y espacios.')
        return apellido
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not re.match(r'^[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}-[0-9kK]$', rut):
            raise forms.ValidationError('El RUT debe tener el formato 12.345.678-9')
        return rut
