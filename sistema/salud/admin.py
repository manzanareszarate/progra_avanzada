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
from .models import medicamento
from .models import receta





# Register your models here.






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


class laboratorioAdmin(admin.ModelAdmin):
    list_display = ('paciente_nombre_apellido', 'fecha', 'hora', 'lugar', 'tipo_Muestra')

    def paciente_nombre_apellido(self, obj):
        return f'{obj.id_paciente.nombre} {obj.id_paciente.apellido}'
    paciente_nombre_apellido.short_description = 'Paciente'
admin.site.register(laboratorio, laboratorioAdmin)

from django.contrib import admin
from .models import medicamento, receta, RecetaMedicamento

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_Medicamento', 'nombre_Medicamento', 'dosis', 'presentacion', 'id_usuario')
    def paciente_nombre_apellido(self, obj):
        return f'{obj.id_paciente.nombre} {obj.id_paciente.apellido}'

admin.site.register(medicamento, MedicamentoAdmin)

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id_Recetas', 'paciente_nombre_apellido', 'fecha_Emision', 'fecha_Reposicion', 'medico', 'lugar', 'id_usuario')
    def paciente_nombre_apellido(self, obj):
        return f'{obj.id_paciente.nombre} {obj.id_paciente.apellido}'
    paciente_nombre_apellido.short_description = 'Paciente' 
admin.site.register(receta, RecetaAdmin)





class RecetaMedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id_receta_medicamento',
        'receta_id',
        'paciente_nombre_apellido',
        'fecha_emision',
        'fecha_reposicion',
        'medico',
        'lugar',
        'medicamento_nombre',
        'medicamento_dosis',
        'medicamento_presentacion',
        'cantidad',
        'frecuencia',
    )

    def receta_id(self, obj):
        return obj.receta.id_Recetas
    receta_id.short_description = 'ID Receta'

    def paciente_nombre_apellido(self, obj):
        return f'{obj.receta.id_paciente.nombre} {obj.receta.id_paciente.apellido}'  
    paciente_nombre_apellido.short_description = 'Paciente'

    def fecha_emision(self, obj):
        return obj.receta.fecha_Emision
    fecha_emision.short_description = 'Fecha Emisión'

    def fecha_reposicion(self, obj):
        return obj.receta.fecha_Reposicion
    fecha_reposicion.short_description = 'Fecha Reposición'

    def medico(self, obj):
        return obj.receta.medico
    medico.short_description = 'Médico'

    def lugar(self, obj):
        return obj.receta.lugar
    lugar.short_description = 'Lugar'

    def medicamento_nombre(self, obj):
        return obj.medicamento.nombre_Medicamento
    medicamento_nombre.short_description = 'Medicamento'

    def medicamento_dosis(self, obj):
        return obj.medicamento.dosis
    medicamento_dosis.short_description = 'Dosis'

    def medicamento_presentacion(self, obj):
        return obj.medicamento.presentacion
    medicamento_presentacion.short_description = 'Presentación'

admin.site.register(RecetaMedicamento, RecetaMedicamentoAdmin)
