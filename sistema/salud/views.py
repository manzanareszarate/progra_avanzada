from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render (request, 'paginas/inicio.html')

def soporte(request):
    return render (request, 'paginas/soporte.html')

def index(request):
    return render (request, 'Programar/index.html')

def agregar(request):
    return render (request, 'Programar/agregar.html')

def editar(request):
    return render (request, 'Programar/editar.html')