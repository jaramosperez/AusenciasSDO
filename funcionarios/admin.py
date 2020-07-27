from django.contrib import admin
from .models import Funcionario

# Register your models here.
class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Funcionario, FuncionarioAdmin)