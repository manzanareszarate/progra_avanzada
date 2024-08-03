from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import cita
from .models import paciente
from .models import laboratorio
from .models import medicamento
from .models import receta  


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


from django import forms
from .models import receta, RecetaMedicamento, medicamento, paciente

from django import forms


class RecetaForm(forms.ModelForm):
    lista_medicamentos = forms.ModelMultipleChoiceField(
        queryset=medicamento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = receta
        fields = ['id_paciente', 'fecha_Emision', 'fecha_Reposicion', 'medico', 'lugar']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=user)  # Filtra pacientes por usuario


class RecetaMedicamentoForm(forms.ModelForm):
    class Meta:
        model = RecetaMedicamento
        fields = ['medicamento', 'cantidad', 'frecuencia']
    
    medicamento = forms.ModelChoiceField(
        queryset=medicamento.objects.none(),
        widget=forms.Select(attrs={'class': 'medicamento-select'})
    )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)
        self.fields['medicamento'].queryset = medicamento.objects.filter(id_usuario=usuario)





#####################################################################################################################
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

