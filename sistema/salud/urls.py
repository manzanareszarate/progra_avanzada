from django.urls import path
from . import views
from .views import login_view, logout_view, inicio, soporte
from .views import registro


urlpatterns = [
path('', views.inicio, name='inicio'),
path('soporte/', views.soporte, name='soporte'),
path('index/', views.index, name='index'),
path('agregar/', views.agregar, name='agregar'),
path('editar/', views.editar, name='editar'),
path ('citas/', views.citas, name='citas'),
path ('laboratorios/', views.laboratorios, name='laboratorios'),
path ('medicamentos/', views.medicamentos, name='medicamentos'),
path ('recetas/', views.recetas, name='recetas'),
path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
path('accounts/login/', login_view, name='login'),
path('accounts/logout/', logout_view, name='logout'),
path('accounts/registro/', registro, name='registro'),
path( 'alertas/', views.alertas, name='alertas')

]