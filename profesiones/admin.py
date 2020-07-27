from django.contrib import admin
from .models import Profesion


# Register your models here.
class ProfesionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')


admin.site.register(Profesion, ProfesionAdmin)
