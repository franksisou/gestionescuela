from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gestorUser.models import Perfil

class Command(BaseCommand):
    help = 'Crea un usuario administrador por defecto'

    def handle(self, *args, **kwargs):
        username = 'admin'
        email = 'admin@escuela.com'
        password = 'admin123'
        
        if not User.objects.filter(username=username).exists():
            # Crear superusuario
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                first_name='Administrador',
                last_name='Sistema'
            )
            
            # Crear perfil
            Perfil.objects.create(usuario=user, rol='admin')
            
            self.stdout.write(self.style.SUCCESS(
                f'✓ Superusuario creado exitosamente:\n'
                f'  Usuario: {username}\n'
                f'  Contraseña: {password}\n'
                f'  Email: {email}'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'El usuario "{username}" ya existe'
            ))
