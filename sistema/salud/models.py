from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True , verbose_name='ID_Paciente')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    sexo = models.CharField(max_length=20, verbose_name='Sexo')
    fecha_nacimiento = models.DateField(null=True, verbose_name='Fecha de Nacimiento')
    edad = models.IntegerField ( verbose_name='Edad')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    telefono = models.IntegerField( verbose_name='Telefono')
    email = models.EmailField( verbose_name='Email')
    
class laboratorios (models.Model):
    id_Laboratorio = models.AutoField(primary_key=True , verbose_name='ID_Laboratorio')
    id_Paciente = models.ForeignKey('paciente', on_delete=models.CASCADE, verbose_name='ID_Paciente')
    fecha = models.DateField(null=False, verbose_name='Fecha')
    hora = models.TimeField(null=False, verbose_name='Hora')
    lugar = models.CharField(max_length=200, verbose_name='Lugar')
    Tipo_Muestra = models.CharField(max_length=50, verbose_name='Tipo de Muestra')







