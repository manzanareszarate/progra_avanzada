from django.urls import path
from . import views
from .views import login_view, logout_view
from .views import registro
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.urls import path
from .views import agregar_alarmas, alarmas, editar_alarmas, eliminar_alarmas






urlpatterns = [
path('', views.inicio, name='inicio'),
path('soporte/', views.soporte, name='soporte'),
path('index/', views.index, name='index'),
path('agregar/', views.agregar, name='agregar'),
path('medicamentos/', views.medicamentos, name='medicamentos'),
path('accounts/login/', login_view, name='login'),
path('accounts/logout/', logout_view, name='logout'),
path('accounts/registro/', registro, name='registro'),
path('alarmas/', views.alarmas, name='alarmas'),
path('editar/<int:paciente_id>/', views.editar, name='editar'),
path('eliminar/<int:paciente_id>/', views.eliminar, name='eliminar'),
path('citas/', views.citas, name='citas'),
path('agregar_cita/', views.agregar_cita, name='agregar_cita'),
path('editar_cita/<int:cita_id>/', views.editar_cita, name='editar_cita'),
path('eliminar_cita/<int:id_Eliminarcita>/', views.eliminar_cita, name='eliminar_cita'),
path('laboratorios/', views.laboratorios, name='laboratorios'),
path('agregar_laboratorio/', views.agregar_laboratorio, name='agregar_laboratorio'),
path('editar_laboratorios/<int:laboratorio_id>/', views.editar_laboratorios, name='editar_laboratorios'),
path('eliminar_laboratorios/<int:id_Eliminarlaboratorios>/', views.eliminar_laboratorios, name='eliminar_laboratorios'),
path('agregar_medicamentos/', views.agregar_medicamentos, name='agregar_medicamentos'),
path('editar_medicamentos/<int:medicamento_id>/', views.editar_medicamentos, name='editar_medicamentos'),
path('eliminar_medicamentos/<int:id_Eliminarmedicamentos>/', views.eliminar_medicamentos, name='eliminar_medicamentos'),
path('recetas', views.recetas, name='recetas'),
path('agregar_receta/', views.agregar_receta, name='agregar_receta'),
path('detalles_receta/<int:receta_id>/', views.detalles_receta, name='detalles_receta'),
path('receta_terminada/<int:receta_id>/',views.receta_terminada, name='receta_terminada'),
path('agregar-alarmas/', views. agregar_alarmas, name='agregar_alarmas'),
path('alarmas/',views. alarmas, name='alarmas'),
path('editar-alarmas/<int:id_alarma>/',views. editar_alarmas, name='editar_alarmas'),
path('eliminar-alarmas/<int:id_alarma>/',views. eliminar_alarmas, name='eliminar_alarmas'),
]

