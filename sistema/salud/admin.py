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
from .models import RecetaMedicamento




# Register your models here.




admin.site.register(Control_Hipertensione)
admin.site.register(Control_Glucosa)
admin.site.register(Control_Peso)
admin.site.register(alarmas)
admin.site.register(RecetaMedicamento)






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


class laboratorioAdmin(admin.ModelAdmin):
    list_display = ('paciente_nombre_apellido', 'fecha', 'hora', 'lugar', 'tipo_Muestra')

    def paciente_nombre_apellido(self, obj):
        return f'{obj.id_paciente.nombre} {obj.id_paciente.apellido}'
    paciente_nombre_apellido.short_description = 'Paciente'

admin.site.register(laboratorio, laboratorioAdmin)


class medicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_Medicamento', 'dosis', 'presentacion', 'id_usuario')

admin.site.register(medicamento, medicamentoAdmin)


class RecetaAdmin(admin.ModelAdmin):
    list_display = ('paciente_nombre_apellido', 'fecha_Emision', 'id_usuario', 'lista_medicamentos')

    def paciente_nombre_apellido(self, obj):
        # Devuelve el nombre completo del paciente
        return f'{obj.id_paciente.nombre} {obj.id_paciente.apellido}'
    paciente_nombre_apellido.short_description = 'Paciente'

    def lista_medicamentos(self, obj):
        # Devuelve una lista de medicamentos asociados, separados por comas
        return ', '.join([medicamento.nombre_Medicamento for medicamento in obj.lista_Medicamentos.all()])
    lista_medicamentos.short_description = 'Medicamentos'

admin.site.register(receta, RecetaAdmin)


