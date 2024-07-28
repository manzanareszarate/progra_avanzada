from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import cita
from .models import paciente

class pacienteForm(forms.ModelForm):#formulario para el modelo paciente
    class Meta:
        model = paciente
        fields = fields = ['cedula', 'nombre', 'apellido', 'sexo', 'fecha_Nacimiento', 'edad', 'direccion', 'telefono', 'email']
        widgets = {
            'fecha_Nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
        }



class CitaForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = ['fecha', 'hora', 'lugar', 'especialidad']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'lugar': forms.TextInput(attrs={'placeholder': 'Lugar de la cita'}),
            'especialidad': forms.TextInput(attrs={'placeholder': 'Especialidad'}),
        }




















class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

