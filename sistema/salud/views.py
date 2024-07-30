from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from .forms import pacienteForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import cita, paciente,laboratorio
from .forms import CitaAgregarForm
from .forms import CitaEditarForm
from .forms import LaboratorioAgregarForm,CitaForm

# Create your views here.


@login_required
def inicio(request):
    return render (request, 'paginas/inicio.html')
@login_required
def soporte(request):
    return render (request, 'paginas/soporte.html')


    
    



@login_required(login_url='/accounts/login/')
def index(request):
    pacientes = paciente.objects.filter(id_usuario=request.user)
    return render(request, 'Programar/index.html', {'pacientes': pacientes})


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




@login_required(login_url='/accounts/login/')
def citas(request):
    # Obtener todas las citas asociadas al usuario actual
    citas = cita.objects.filter(id_usuario=request.user)

    context = {
        'citas': citas
    }

    return render(request, 'Programar/citas.html', context)


#agregar una cita
# views.py

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



###################################################################################################################



































































def medicamentos (request):
    return render (request, 'Programar/medicamentos.html')

def recetas(request):
    return render (request, 'Programar/recetas.html')


####################################################################################################3
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



