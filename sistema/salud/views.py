from django.forms import inlineformset_factory
from .models import receta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import receta, medicamento
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .models import receta, medicamento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import cita, paciente,laboratorio,medicamento
from .forms import CitaAgregarForm
from .forms import CitaEditarForm
from .forms import LaboratorioAgregarForm
from .forms import Laboratorioeditarform
from .forms import MedicamentoForm
from .forms import EditarMedicamentoForm, pacienteForm,RecetaMedicamento


# Create your views here.


@login_required
def inicio(request):
    return render (request, 'paginas/inicio.html')
@login_required
def soporte(request):
    return render (request, 'paginas/soporte.html')


    
    


##############################################################################################################3
###### ver pacientes
@login_required(login_url='/accounts/login/')
def index(request):
    pacientes = paciente.objects.filter(id_usuario=request.user)
    return render(request, 'Programar/index.html', {'pacientes': pacientes})

##############################################################################################################3
#agrergar un paciente     
login_required(login_url='/accounts/login/')
def agregar(request):
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            # Asignar la instancia del usuario actual
            instancia.id_usuario = request.user
            instancia.save()
            return redirect('index')  # Redirige a la página de inicio o a la página deseada
    else:
        form = pacienteForm()
    
    return render(request, 'Programar/agregar.html', {'form': form})

##############################################################################################################3
#vista para editar un paciente


@login_required(login_url='/accounts/login/')
def editar(request, paciente_id):
    # Obtener la instancia del paciente o devolver 404 si no se encuentra
    paciente_instance = get_object_or_404(paciente, id_paciente=paciente_id)

    # Verificar que el paciente pertenece al usuario actual
    if paciente_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    if request.method == 'POST':
        form = pacienteForm(request.POST, instance=paciente_instance)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.id_usuario = request.user  # Mantener el usuario actual
            instancia.save()
            return redirect('index')  # Redirige a la página de inicio o a la página deseada
    else:
        form = pacienteForm(instance=paciente_instance)

    return render(request, 'Programar/editar.html', {'form': form, 'paciente': paciente_instance})

##############################################################################################################3
#vista para eliminar un paciente

@login_required(login_url='/accounts/login/')
def eliminar(request, paciente_id):
    # Obtener la instancia del paciente o devolver 404 si no se encuentra
    paciente_instance = get_object_or_404(paciente, id_paciente=paciente_id)

    # Verificar que el paciente pertenece al usuario actual
    if paciente_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    if request.method == 'POST':
        paciente_instance.delete()  # Eliminar el paciente
        return redirect('index')  # Redirige a la página de inicio o a la página deseada

    return render(request, 'Programar/eliminar.html', {'paciente': paciente_instance})


###########################################################################################################3
###### vistas para citas 



##############################################################################################################3
#ver citas
@login_required(login_url='/accounts/login/')
def citas(request):
    # Obtener todas las citas asociadas al usuario actual
    citas = cita.objects.filter(id_usuario=request.user)

    context = {
        'citas': citas
    }

    return render(request, 'Programar/citas.html', context)


##############################################################################################################3
#agregar cita

@login_required(login_url='/accounts/login/')
def agregar_cita(request):
    if request.method == 'POST':
        form = CitaAgregarForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.id_usuario = request.user  # Asigna el usuario actual (si corresponde)
            instancia.save()
            return redirect('citas')  # Redirige a la página de citas
    else:
        form = CitaAgregarForm()
        # Filtra los pacientes para el usuario autenticado
        form.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=request.user)
    
    return render(request, 'Programar/agregar_cita.html', {'form': form})
###########3##############################################################################################################3
#modificar cita

@login_required(login_url='/accounts/login/')
def editar_cita(request, cita_id):
    # Obtener la instancia de la cita o devolver 404 si no se encuentra
    cita_instance = get_object_or_404(cita, id_Cita=cita_id)

    # Verificar que la cita pertenece al usuario actual
    if cita_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    if request.method == 'POST':
        form = CitaEditarForm(request.POST, instance=cita_instance)
        form.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=request.user)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.id_usuario = request.user  # Mantener el usuario actual
            instancia.save()
            return redirect('citas')  # Redirige a la página de inicio o a la página deseada
    else:
        form = CitaEditarForm(instance=cita_instance)
        form.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=request.user)

    return render(request, 'Programar/editar_cita.html', {'form': form, 'cita': cita_instance})

##############################################################################################################3
#eliminar cita


@login_required(login_url='/accounts/login/')
def eliminar_cita(request, id_Eliminarcita):
    # Obtener la instancia de la cita o devolver 404 si no se encuentra
    citaeliminar_instance = get_object_or_404(cita, id_Cita=id_Eliminarcita)

    # Verificar que la cita pertenece al usuario actual
    if citaeliminar_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    # Obtener el paciente asociado
    paciente_instance = citaeliminar_instance.id_paciente
    
    

    if request.method == 'POST':
        citaeliminar_instance.delete()  # Eliminar la cita
        return redirect('citas')  # Redirige a la página de citas o a la página deseada

    # Pasar los detalles de la cita y del paciente a la plantilla
    context = {
        'cita': citaeliminar_instance,
        'paciente': paciente_instance
    }
    return render(request, 'Programar/eliminar_cita.html', context)




############################################ver laboratorios ########################################################
##############################################################################################################3
#ver laboratorios


@login_required(login_url='/accounts/login/')
def laboratorios(request):
    # Obtener todos los laboratorios asociados al usuario actual
    laboratorios = laboratorio.objects.filter(id_usuario=request.user)

    context = {
        'laboratorios': laboratorios
    }

    return render(request, 'Programar/laboratorios.html', context)



##############################################################################################################3

#agrergar un laboratorio
@login_required(login_url='/accounts/login/')
def agregar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioAgregarForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.id_usuario = request.user  # Asigna el usuario actual (si corresponde)
            instancia.save()
            return redirect('laboratorios')  # Redirige a la página de citas
    else:
        form = LaboratorioAgregarForm()
        # Filtra los pacientes para el usuario autenticado
        form.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=request.user)
    
    return render(request, 'Programar/agregar_laboratorio.html', {'form': form})



###################################################################################################################
#editar laboratorio



@login_required(login_url='/accounts/login/')
def editar_laboratorios(request, laboratorio_id):
    # Obtener la instancia de la cita o devolver 404 si no se encuentra
    laboratorio_instance = get_object_or_404(laboratorio, id_Laboratorios=laboratorio_id)

    # Verificar que el laboratorio pertenece al usuario actual
    if laboratorio_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    if request.method == 'POST':
        form = Laboratorioeditarform (request.POST, instance=laboratorio_instance)
        form.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=request.user)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.id_usuario = request.user  # Mantener el usuario actual
            instancia.save()
            return redirect('laboratorios')  # Redirige a la página de inicio o a la página deseada
    else:
        form = Laboratorioeditarform (instance=laboratorio_instance)
        form.fields['id_paciente'].queryset = paciente.objects.filter(id_usuario=request.user)

    return render(request,'Programar/editar_laboratorios.html', {'form': form, 'laboratorio': laboratorio_instance})

###################################################################################################################

#Eliminar laboratorio


@login_required(login_url='/accounts/login/')
def eliminar_laboratorios(request, id_Eliminarlaboratorios):
    # Obtener la instancia de la cita o devolver 404 si no se encuentra
    laboratorioeliminar_instance = get_object_or_404(laboratorio, id_Laboratorios=id_Eliminarlaboratorios)

    # Verificar que la cita pertenece al usuario actual
    if laboratorioeliminar_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    # Obtener el paciente asociado
    paciente_instance = laboratorioeliminar_instance.id_paciente
    
    

    if request.method == 'POST':
        laboratorioeliminar_instance.delete()  # Eliminar la cita
        return redirect('laboratorios')  # Redirige a la página de citas o a la página deseada

    # Pasar los detalles de la cita y del paciente a la plantilla
    context = {
        'laboratorio': laboratorioeliminar_instance,
        'paciente': paciente_instance
    }
    return render(request, 'Programar/eliminar_laboratorios.html', context)

##############################################################################################################3

#ver medicamentos

@login_required(login_url='/accounts/login/')
def medicamentos(request):
    # Obtener todos los medicamentos asociados al usuario actual
    medicamentos = medicamento.objects.filter(id_usuario=request.user)

    context = {
        'medicamentos': medicamentos
    }

    return render(request, 'Programar/medicamentos.html', context)
##############################################################################################################################
#agregar medicamentos
@login_required(login_url='/accounts/login/')
def agregar_medicamentos(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            medicamento = form.save(commit=False)
            medicamento.id_usuario = request.user
            medicamento.save()
            return redirect('medicamentos')  # Cambia a la vista a la que quieras redirigir
    else:
        form = MedicamentoForm()

    return render(request, 'Programar/agregar_medicamentos.html', {'form': form})



##############################################################################################################3
########3 editar medicamentos

@login_required(login_url='/accounts/login/')
def editar_medicamentos(request, medicamento_id):
    # Obtener la instancia del medicamento o devolver 404 si no se encuentra
    medicamento_instance = get_object_or_404(medicamento, id_Medicamento=medicamento_id)

    # Verificar que el medicamento pertenece al usuario actual
    if medicamento_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    if request.method == 'POST':
        form = EditarMedicamentoForm (request.POST, instance=medicamento_instance)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.id_usuario = request.user  # Mantener el usuario actual
            instancia.save()
            return redirect('medicamentos')  # Redirige a la página de inicio o a la página deseada
    else:
        form = EditarMedicamentoForm (instance=medicamento_instance)
        

    return render(request,'Programar/editar_medicamentos.html', {'form': form, 'medicamento': medicamento_instance})

##########33##############################################################################################################3
########3 eliminar medicamentos
    
@login_required(login_url='/accounts/login/')
def eliminar_medicamentos(request, id_Eliminarmedicamentos):
    # Obtener la instancia de la cita o devolver 404 si no se encuentra
    medicamentoeliminar_instance = get_object_or_404(medicamento, id_Medicamento=id_Eliminarmedicamentos)

    # Verificar que la cita pertenece al usuario actual
    if medicamentoeliminar_instance.id_usuario != request.user:
        return redirect('inicio')  # Redirige a una página de error o a una página de acceso denegado

    
    if request.method == 'POST':
        medicamentoeliminar_instance.delete()  # Eliminar la cita
        return redirect('medicamentos')  # Redirige a la página de citas o a la página deseada

    # Pasar los detalles de la cita y del paciente a la plantilla
    context = {
        'medicamento': medicamentoeliminar_instance,
        
    }
    return render(request, 'Programar/eliminar_medicamentos.html', context)





##############################################################################################################3
########3 ver recetas
@login_required
def recetas(request):
    # Obtén todas las recetas asociadas al usuario logueado
    recetas = receta.objects.filter(id_usuario=request.user)
    
    return render(request, 'Programar/recetas.html', {'recetas': recetas})




##############################################################################################################3
@login_required
def agregar_receta(request):
    if request.method == 'POST':
        id_paciente = request.POST.get('id_paciente')
        fecha_emision = request.POST.get('fecha_Emision')
        fecha_reposicion = request.POST.get('fecha_Reposicion')
        lugar = request.POST.get('lugar')
        medico = request.POST.get('medico')
        medicamentos_ids = request.POST.get('medicamentos_ids').split(',')
        
        # Validación básica
        if not id_paciente or not fecha_emision or not fecha_reposicion or not lugar or not medico:
            messages.error(request, 'Por favor, complete todos los campos requeridos.')
            return redirect('agregar_receta')  # Redirige a la misma página

        # Crear una nueva receta
        receta_nueva = receta(
            id_paciente_id=id_paciente,
            fecha_Emision=fecha_emision,
            fecha_Reposicion=fecha_reposicion,
            medico=medico,  # Guardamos el nombre del médico ingresado
            lugar=lugar,
            id_usuario=request.user
        )
        receta_nueva.save()

        # Agregar medicamentos a la receta
        for medicamento_id in medicamentos_ids:
            if medicamento_id:  # Asegúrate de que el ID no esté vacío
                medicamento_obj = medicamento.objects.get(id_Medicamento=medicamento_id)
                cantidad = request.POST.get('cantidad', None)
                frecuencia = request.POST.get('frecuencia', None)

                # Solo agrega los campos si no están vacíos
                RecetaMedicamento.objects.create(
                    receta=receta_nueva,
                    medicamento=medicamento_obj,
                    cantidad=cantidad if cantidad else None,
                    frecuencia=frecuencia if frecuencia else None,
                    usuario=request.user
                )

        messages.success(request, 'Receta agregada exitosamente.')
        return redirect('recetas')  # Redirige a la lista de recetas

    # Filtra pacientes por el usuario actual
    pacientes = paciente.objects.filter(id_usuario=request.user)  # Filtra solo los pacientes del usuario
    medicamentos = medicamento.objects.all()
    return render(request, 'Programar/agregar_receta.html', {'pacientes': pacientes, 'medicamentos': medicamentos})



from django.shortcuts import render, get_object_or_404
from .models import receta  # Asegúrate de importar el modelo correcto

def detalle_receta(request, receta_id):
    receta = get_object_or_404(receta, id_Receta=receta_id)
    return render(request, 'Programacion/detalles_receta.html', {'receta': receta})



####################################################################################################3
###login y registro
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('inicio')

def alarmas (request):
    return render (request, 'Programar/alarmas.html')