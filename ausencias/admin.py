from django.contrib import admin
from .models import Ausencia

# Register your models here.
class AusenciaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Ausencia, AusenciaAdmin)