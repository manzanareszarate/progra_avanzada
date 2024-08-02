from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import cita
from .models import paciente
from .models import laboratorio
from .models import medicamento
from .models import receta  
from .models import receta_medicamento

from django.forms import inlineformset_factory, BaseFormSet, formset_factory

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

# form para agregar citas
class CitaAgregarForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = ['id_paciente', 'fecha', 'hora', 'lugar', 'especialidad']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    # Se puede agregar un método para personalizar el campo de selección si es necesario
    id_paciente = forms.ModelChoiceField(
        queryset=paciente.objects.all(),
        empty_label="Selecciona un paciente",
        label="Nombre del Paciente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    #Editar citas
class CitaEditarForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = ['id_paciente', 'fecha', 'hora', 'lugar', 'especialidad']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    id_paciente = forms.ModelChoiceField(
        queryset=paciente.objects.none(),  # Inicialmente vacío
        empty_label="Selecciona un paciente",
        label="Nombre del Paciente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

#Mostar Laboratorios

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = laboratorio
        fields = ['fecha', 'hora', 'lugar', 'tipo_Muestra']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'lugar': forms.TextInput(attrs={'placeholder': 'Lugar del laboratorio'}),
            'tipo_Muestra': forms.TextInput(attrs={'placeholder': 'Tipo de muestra'}),
        }


#agregar laboratorio

class LaboratorioAgregarForm(forms.ModelForm):
    class Meta:
        model = laboratorio
        fields = ['id_paciente', 'fecha', 'hora', 'lugar', 'tipo_Muestra']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'lugar': forms.TextInput(attrs={'placeholder': 'Lugar del laboratorio'}),
            'tipo_Muestra': forms.TextInput(attrs={'placeholder': 'Tipo de muestra'}),
        }
    
    # Se puede agregar un método para personalizar el campo de selección si es necesario
    id_paciente = forms.ModelChoiceField(
        queryset=paciente.objects.all(),
        empty_label="Selecciona un paciente",
        label="Nombre del Paciente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    

##############################################################################################################

#Editar Laboratorio

class Laboratorioeditarform(forms.ModelForm):
    class Meta:
        model = laboratorio
        fields = ['id_paciente', 'fecha', 'hora', 'lugar', 'tipo_Muestra']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'lugar': forms.TextInput(attrs={'placeholder': 'Lugar del laboratorio'}),
            'tipo_Muestra': forms.TextInput(attrs={'placeholder': 'Tipo de muestra'}),
        }
    
    # Se puede agregar un método para personalizar el campo de selección si es necesario
    id_paciente = forms.ModelChoiceField(
        queryset=paciente.objects.all(),
        empty_label="Selecciona un paciente",
        label="Nombre del Paciente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )



######## agregar medicamentos 


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = medicamento
        fields = ['nombre_Medicamento', 'dosis','presentacion',]

#editar Medicamentos


class EditarMedicamentoForm(forms.ModelForm):
    class Meta:
        model = medicamento
        fields = ['nombre_Medicamento', 'dosis','presentacion',]


################################################################################################3

####Agregar  receta  y recetamedicamento form ################################

#######################################################################################################3




class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = medicamento
        fields = ['nombre_Medicamento', 'dosis', 'presentacion']
        widgets = {
            'nombre_Medicamento': forms.TextInput(attrs={'placeholder': 'Nombre del medicamento'}),
            'dosis': forms.TextInput(attrs={'placeholder': 'Dosis'}),
            'presentacion': forms.TextInput(attrs={'placeholder': 'Presentación'}),
        }

##############################################################################################################
#agregar receta
# forms.py

from django import forms
from .models import receta, medicamento, receta_medicamento, paciente

class RecetaForm(forms.ModelForm):
    class Meta:
        model = receta
        fields = ['id_paciente', 'fecha_Emision', 'fecha_Reposicion', 'lista_Medicamentos', 'medico', 'lugar']
        widgets = {
            'lista_Medicamentos': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=user)
            self.fields['lista_Medicamentos'].queryset = medicamento.objects.filter(id_usuario=user)

    def clean(self):
        cleaned_data = super().clean()
        medicamentos = cleaned_data.get('lista_Medicamentos')
        if medicamentos:
            medicamento_ids = [med.id for med in medicamentos]
            if len(medicamento_ids) != len(set(medicamento_ids)):
                raise forms.ValidationError("No se pueden repetir medicamentos en una misma receta.")
        return cleaned_data





















#####################################################################################################################
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

