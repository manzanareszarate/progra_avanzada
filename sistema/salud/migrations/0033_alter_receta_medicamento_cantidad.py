# Generated by Django 5.0.7 on 2024-07-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0032_receta_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta_medicamento',
            name='cantidad',
            field=models.CharField(max_length=50, verbose_name='Cantidad'),
        ),
    ]