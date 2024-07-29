from django.contrib import admin
from .models import paciente
from .models import laboratorio
from .models import cita
from .models import medicamento
from .models import receta
from .models import Control_Hipertensione
from .models import Control_Glucosa
from .models import Control_Peso
from .models import alarmas





# Register your models here.

admin.site.register(laboratorio)
admin.site.register(medicamento)
admin.site.register(receta)
admin.site.register(Control_Hipertensione)
admin.site.register(Control_Glucosa)
admin.site.register(Control_Peso)
admin.site.register(alarmas)





class citaAdmin(admin.ModelAdmin):
    list_display = ('paciente_nombre_apellido', 'fecha', 'hora', 'lugar', 'especialidad')

    def paciente_nombre_apellido(self, obj):
        return f'{obj.id_paciente.nombre} {obj.id_paciente.apellido}'
    paciente_nombre_apellido.short_description = 'Paciente'

admin.site.register(cita, citaAdmin)




class pacienteAdmin(admin.ModelAdmin):
    list_display = (
        'cedula', 'nombre', 'apellido', 'sexo', 'fecha_Nacimiento', 
        'edad', 'direccion', 'telefono', 'email', 'id_usuario')
    
admin.site.register(paciente, pacienteAdmin)

