# Generated by Django 5.0.7 on 2024-07-27 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0016_paciente_id_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='id_usuario',
            new_name='id_usuari',
        ),
    ]