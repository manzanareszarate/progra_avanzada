# Generated by Django 5.0.7 on 2024-07-28 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0024_rename_alertas_alarmas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmas',
            name='id_Paciente',
        ),
        migrations.RemoveField(
            model_name='cita',
            name='id_Usuario',
        ),
        migrations.RemoveField(
            model_name='control_glucosa',
            name='id_Usuario',
        ),
        migrations.RemoveField(
            model_name='control_hipertensione',
            name='id_Usuario',
        ),
        migrations.RemoveField(
            model_name='control_peso',
            name='id_Usuario',
        ),
        migrations.RemoveField(
            model_name='laboratorio',
            name='id_Paciente',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='id_Usuario',
        ),
        migrations.AddField(
            model_name='cita',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='control_glucosa',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='control_hipertensione',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='control_peso',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receta',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alarmas',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salud.paciente'),
            preserve_default=False,
        ),
    ]
