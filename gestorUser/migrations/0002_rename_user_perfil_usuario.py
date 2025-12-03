# Generated manually

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestorUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='user',
            new_name='usuario',
        ),
    ]
