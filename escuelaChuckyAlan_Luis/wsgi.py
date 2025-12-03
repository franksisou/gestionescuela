"""
WSGI config for escuelaChuckyAlan_Luis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escuelaChuckyAlan_Luis.settings')

application = get_wsgi_application()
