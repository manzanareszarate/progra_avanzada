# Generated by Django 5.0.7 on 2024-07-27 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0022_rename_id_alerta_alertas_id_alertas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alertas',
            old_name='id_alertas',
            new_name='id_Alertas',
        ),
    ]
