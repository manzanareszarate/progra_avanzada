from django.shortcuts import render
from models import paciente


# Create your views here.

def inicio(request):
    return render (request, 'paginas/inicio.html')

def soporte(request):
    return render (request, 'paginas/soporte.html')

def index(request):
    paciente = paciente.objects.all()
    return render (request, 'Programar/index.html', {'paciente':paciente})

def agregar(request):
    return render (request, 'Programar/agregar.html')

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