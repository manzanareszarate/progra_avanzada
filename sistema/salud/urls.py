from django.urls import path
from . import views
from .views import login_view, logout_view
from .views import registro
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.urls import path
from django.urls import include

urlpatterns = [
path('', views.inicio, name='inicio'),
path('soporte/', views.soporte, name='soporte'),
path('index/', views.index, name='index'),
path('agregar/', views.agregar, name='agregar'),
path('medicamentos/', views.medicamentos, name='medicamentos'),
path('recetas/', views.recetas, name='recetas'),
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


]