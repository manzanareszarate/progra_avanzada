from django.db import models

# Create your models here.
class paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True , verbose_name='ID_Paciente')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    sexo = models.CharField(max_length=20, verbose_name='Sexo')
    fecha_nacimiento = models.DateField( verbose_name='Fecha de Nacimiento')
    edad = models.IntegerField ( verbose_name='Edad')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    telefono = models.IntegerField( verbose_name='Telefono')
    email = models.EmailField( verbose_name='Email')
    