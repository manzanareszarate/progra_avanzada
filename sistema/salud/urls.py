from django.urls import path
from . import views
from .views import login_view, logout_view
from .views import registro
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.urls import path
#from .views import CitaListView
from .views import cita

urlpatterns = [
path('', views.inicio, name='inicio'),
path('soporte/', views.soporte, name='soporte'),
path('index/', views.index, name='index'),
path('agregar/', views.agregar, name='agregar'),
path ('laboratorios/', views.laboratorios, name='laboratorios'),
path ('medicamentos/', views.medicamentos, name='medicamentos'),
path ('recetas/', views.recetas, name='recetas'),
path('accounts/login/', login_view, name='login'),
path('accounts/logout/', logout_view, name='logout'),
path('accounts/registro/', registro, name='registro'),
path('alarmas/', views.alarmas, name='alarmas'),
path('editar/<int:paciente_id>/', views.editar, name='editar'),
path('eliminar/<int:paciente_id>/', views.eliminar, name='eliminar'),
#path('citas/', CitaListView.as_view(), name='citas_list'),
path('citas/', views.citas, name='citas'),

]