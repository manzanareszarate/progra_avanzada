# Generated by Django 5.0.7 on 2024-07-27 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0017_rename_id_usuario_paciente_id_usuari'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='id_usuari',
            new_name='id_usuario',
        ),
    ]