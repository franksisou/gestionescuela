from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Perfil

class FormularioRegistro(UserCreationForm):
    # Validador para nombre y apellido (solo letras y espacios)
    nombre_validator = RegexValidator(
        regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
        message='Solo se permiten letras y espacios'
    )
    
    # Validador para email (palabras, números y @)
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Ingrese un correo electrónico válido'
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        validators=[nombre_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre'
        }),
        label='Nombre'
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        validators=[nombre_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su apellido'
        }),
        label='Apellido'
    )
    
    email = forms.EmailField(
        required=True,
        validators=[email_validator],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com'
        }),
        label='Correo Electrónico'
    )
    
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre de usuario'
        }),
        label='Nombre de Usuario'
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña'
        }),
        label='Contraseña'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña'
        }),
        label='Confirmar Contraseña'
    )
    
    rol = forms.ChoiceField(choices=[('usuario', 'Usuario')])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'rol']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.replace(' ', '').isalpha():
            raise forms.ValidationError('El nombre solo debe contener letras')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.replace(' ', '').isalpha():
            raise forms.ValidationError('El apellido solo debe contener letras')
        return last_name
