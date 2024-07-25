from django.contrib import admin
from .models import paciente
from .models import laboratorio
from .models import cita
from .models import medicamento
from .models import recetas
from .models import Control_Hipertension
from .models import Control_Glucosa
from .models import Control_Peso






# Register your models here.
admin.site.register(paciente)
admin.site.register(laboratorio)
admin.site.register(cita)
admin.site.register(medicamento)
admin.site.register(recetas)
admin.site.register(Control_Hipertension)
admin.site.register(Control_Glucosa)
admin.site.register(Control_Peso)

