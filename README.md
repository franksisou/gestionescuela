# Sistema de Gestión Escolar

Sistema web para la gestión de cursos y alumnos desarrollado con Django.

## Requisitos Previos

- Python 3.8 o superior
- MySQL Server
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/franksisou/gestionescuela.git
cd gestionescuela
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Linux/Mac
```

### 3. Instalar dependencias

```bash
pip install django pymysql
```

### 4. Configurar la base de datos

Crea una base de datos MySQL llamada `escuela_chucky_alan_luis1`:

```sql
CREATE DATABASE escuela_chucky_alan_luis1;
```

Si necesitas cambiar las credenciales de MySQL, edita el archivo `escuelaChuckyAlan_Luis/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'escuela_chucky_alan_luis1',
        'USER': 'root',  # Tu usuario de MySQL
        'PASSWORD': ''   # Tu contraseña de MySQL
    }
}
```

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Crear usuario administrador

```bash
python manage.py crear_admin
```

Este comando creará automáticamente un usuario administrador con las siguientes credenciales:

- **Usuario:** admin
- **Contraseña:** admin123
- **Email:** admin@escuela.com

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

El sistema estará disponible en: http://127.0.0.1:8000/

## Usuarios de Prueba

### Administrador

- **Usuario:** admin
- **Contraseña:** admin123
- **Permisos:** Acceso completo al sistema

## Estructura del Proyecto

```
escuelaChuckyAlan_Luis/
├── gestorCursos/          # App de gestión de cursos y alumnos
├── gestorUser/            # App de autenticación y perfiles
├── templates/             # Plantillas HTML
├── static/               # Archivos estáticos (CSS, JS, imágenes)
└── escuelaChuckyAlan_Luis/  # Configuración del proyecto
```

## Funcionalidades

- ✅ Registro e inicio de sesión de usuarios
- ✅ Gestión de cursos (CRUD)
- ✅ Gestión de alumnos (CRUD)
- ✅ Dashboard administrativo con estadísticas
- ✅ Relación alumno-curso
- ✅ Control de acceso basado en roles
- ✅ Interfaz responsive con Bootstrap 5

## Tecnologías Utilizadas

- **Backend:** Django 5.0
- **Base de Datos:** MySQL
- **Frontend:** Bootstrap 5.3.7
- **Templates:** Landify & Flexy
- **Icons:** Bootstrap Icons

## Soporte

Si tienes problemas con la instalación o ejecución del proyecto, verifica:

1. Que MySQL esté ejecutándose
2. Que las credenciales de la base de datos sean correctas
3. Que todas las dependencias estén instaladas
4. Que hayas aplicado las migraciones

## Licencia

Este proyecto fue desarrollado con fines educativos.
