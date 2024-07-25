from django import forms
from .models import paciente

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'