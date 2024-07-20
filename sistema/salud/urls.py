from django.urls import path
from . import views


urlpatterns = [
path('', views.inicio, name='inicio'),
path('soporte/', views.soporte, name='soporte'),
path('index/', views.index, name='index'),
path('agregar/', views.agregar, name='agregar'),
path('editar/', views.editar, name='editar')
]


