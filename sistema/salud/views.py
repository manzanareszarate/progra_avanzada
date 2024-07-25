from django.shortcuts import render
from .models import paciente
from .forms import pacienteForm



# Create your views here.

def inicio(request):
    return render (request, 'paginas/inicio.html')

def soporte(request):
    return render (request, 'paginas/soporte.html')

def index(request):
    pacientes = paciente.objects.all()
    return render (request, 'Programar/index.html', context={'pacientes':pacientes})
    




def agregar(request):
    formulario = pacienteForm(request.POST or None)
    return render (request, 'Programar/agregar.html',{'form':formulario})


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