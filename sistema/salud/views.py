from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import paciente
from .forms import pacienteForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistroForm




# Create your views here.


@login_required
def inicio(request):
    return render (request, 'paginas/inicio.html')
@login_required
def soporte(request):
    return render (request, 'paginas/soporte.html')
@login_required
def index(request):
    pacientes = paciente.objects.all()
    return render (request, 'Programar/index.html', context={'pacientes':pacientes})
    
def agregar(request):
    form = pacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render (request, 'Programar/agregar.html', {'form':form})

def eliminar(request, id):
    elimina_paciente= paciente.objects.get(id_paciente=id)
    elimina_paciente.delete()
    return redirect('index')

def editar(request):
    return render (request, 'Programar/editar.html')

def citas(request):
    return render (request, 'Programar/citas.html')

def laboratorios(request):
    return render (request, 'Programar/laboratorios.html')

def medicamentos (request):
    return render (request, 'Programar/medicamentos.html')

def recetas(request):
    return render (request, 'Programar/recetas.html')

###############################
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
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('inicio')


