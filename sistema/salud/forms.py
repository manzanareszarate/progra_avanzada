from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import paciente

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['cedula', 'nombre', 'apellido', 'sexo', 'fecha_Nacimiento', 'edad', 'direccion', 'telefono', 'email',]	























class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

