"""
Script para crear perfiles de usuario faltantes
Ejecutar con: python manage.py shell < crear_perfiles_faltantes.py
"""

from django.contrib.auth.models import User
from gestorUser.models import Perfil

# Obtener todos los usuarios
usuarios = User.objects.all()

creados = 0
for usuario in usuarios:
    # Intentar obtener o crear el perfil
    perfil, created = Perfil.objects.get_or_create(
        usuario=usuario,
        defaults={'rol': 'usuario'}
    )
    
    if created:
        creados += 1
        print(f"✅ Perfil creado para: {usuario.username}")
    else:
        print(f"ℹ️  {usuario.username} ya tiene perfil (rol: {perfil.rol})")

print(f"\n🎉 Total de perfiles creados: {creados}")
print(f"📊 Total de usuarios en sistema: {usuarios.count()}")
