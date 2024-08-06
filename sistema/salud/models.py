from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True , verbose_name='ID_Paciente')
    cedula = models.IntegerField(null=True,verbose_name='Cedula')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    sexo = models.CharField(max_length=20, verbose_name='Sexo')
    fecha_Nacimiento = models.DateField(null=True, verbose_name='Fecha de Nacimiento')
    edad = models.IntegerField ( verbose_name='Edad')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    telefono = models.IntegerField( verbose_name='Telefono')
    email = models.EmailField( verbose_name='Email')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"{self.nombre} {self.apellido}"


#########################################################



class cita(models.Model):
    id_Cita = models.AutoField(primary_key=True , verbose_name='ID_Cita')
    id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, verbose_name='Fecha')
    hora = models.TimeField(null=False, verbose_name='Hora')
    lugar = models.CharField(max_length=200, verbose_name='Lugar')
    especialidad = models.CharField(max_length=50, verbose_name='Especialidad')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

def __str__(self):
        return f"{self.fecha} {self.hora} {self.lugar} {self.especialidad}"




#################################################################################
class laboratorio (models.Model):
    id_Laboratorios = models.AutoField(primary_key=True , verbose_name='ID_Laboratorio')
    id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, verbose_name='Fecha')
    hora = models.TimeField(null=False, verbose_name='Hora')
    lugar = models.CharField(max_length=200, verbose_name='Lugar')
    tipo_Muestra = models.CharField(max_length=50, verbose_name='Tipo de Muestra')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
        return f"{self.fecha} {self.hora} {self.lugar} {self.tipo_Muestra}"


########################################################################################

class medicamento(models.Model):
    id_Medicamento = models.AutoField(primary_key=True, verbose_name='ID_Medicamento')
    nombre_Medicamento = models.CharField(max_length=50, verbose_name='Nombre')
    dosis = models.CharField(max_length=50, verbose_name='Dosis')
    presentacion = models.CharField(max_length=50, verbose_name='Presentacion')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_Medicamento} {self.dosis} {self.presentacion}"

class receta(models.Model):
    id_Recetas = models.AutoField(primary_key=True, verbose_name='ID_Recetas')
    id_paciente = models.ForeignKey('paciente', on_delete=models.CASCADE)  # Asegúrate de que 'paciente' exista
    fecha_Emision = models.DateField(null=False, verbose_name='Fecha_Emision')
    fecha_Reposicion = models.DateField(null=False, verbose_name='Fecha_Reposicion')
    medico = models.CharField(max_length=50, verbose_name='Medico')
    lugar = models.CharField(max_length=200, verbose_name='Lugar')
    medicamentos = models.ManyToManyField(medicamento, through='RecetaMedicamento')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha_Emision} {self.fecha_Reposicion} {self.medico} {self.lugar}"

class RecetaMedicamento(models.Model):
    id_receta_medicamento = models.AutoField(primary_key=True, verbose_name='ID_Receta_Medicamento')
    receta = models.ForeignKey(receta, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    frecuencia = models.CharField(max_length=50, verbose_name='Frecuencia')
    

    class Meta:
        unique_together = ('receta', 'medicamento')  # Asegura que la combinación sea única

    def __str__(self):
        return f"{self.medicamento.nombre_Medicamento} - Cantidad: {self.cantidad} - Frecuencia: {self.frecuencia}"



###########################################################################################








    ###########################################################################################





class Control_Hipertensione (models.Model):
        id_Hipertension = models.AutoField(primary_key=True , verbose_name='ID_Hipertension')
        id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
        fecha = models.DateField(null=False, verbose_name='Fecha')
        diastolica = models.IntegerField ( verbose_name='Diastolica')
        sistolica = models.IntegerField ( verbose_name='Sistolica')
    
    

class Control_Glucosa(models.Model):
    id_Glucosa = models.AutoField(primary_key=True , verbose_name='ID_Glucosa')
    id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, verbose_name='Fecha')
    glisemia = models.IntegerField ( verbose_name='Glisemia')

class Control_Peso(models.Model):
    id_Peso = models.AutoField(primary_key=True , verbose_name='ID_Peso')
    id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, verbose_name='Fecha')
    Peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso')
    Altura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Altura')
    IMC = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='IMC')








from datetime import timedelta

class alarmas(models.Model):
    ALARMA_TIPO = (
        ('cita', 'Cita Médica'),
        ('laboratorio', 'Laboratorio'),
        ('receta', 'Receta Médica'),
    )
    
    MEDIO_NOTIFICACION = (
        ('email', 'Correo Electrónico'),
        ('whatsapp', 'WhatsApp'),
        ('sms', 'SMS'),
    )
    
    FRECUENCIA_OPCIONES = (
        ('1 hora', '1 hora'),
        ('1 día', '1 día'),
        ('1 semana', '1 semana'),
        ('1 mes', '1 mes'),
    )
    
    id_alarma = models.AutoField(primary_key=True, verbose_name='ID_Alarma')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    id_paciente = models.ForeignKey('paciente', on_delete=models.CASCADE, verbose_name='Paciente')
    fecha_alarma = models.DateTimeField(verbose_name='Fecha y Hora de la Alarma')
    frecuencia = models.CharField(max_length=20, choices=FRECUENCIA_OPCIONES, verbose_name='Frecuencia')
    medio_notificacion = models.CharField(max_length=20, choices=MEDIO_NOTIFICACION, verbose_name='Medio de Notificación')
    activa = models.BooleanField(default=True, verbose_name='Activa')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f"Alarma para {self.id_paciente} - {self.id_usuario.username} - {self.fecha_alarma}"

    class Meta:
        verbose_name = 'Alarma'
        verbose_name_plural = 'Alarmas'
        ordering = ['fecha_alarma']

    def calcular_fecha_notificacion(self):
        """Calcula la fecha de notificación basada en la frecuencia."""
        if self.frecuencia == '1 hora':
            return self.fecha_alarma - timedelta(hours=1)
        elif self.frecuencia == '1 día':
            return self.fecha_alarma - timedelta(days=1)
        elif self.frecuencia == '1 semana':
            return self.fecha_alarma - timedelta(weeks=1)
        elif self.frecuencia == '1 mes':
            return self.fecha_alarma - timedelta(days=30)  # Considera un mes como 30 días
        return self.fecha_alarma  # Si no coincide, retorna la fecha original