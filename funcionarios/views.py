from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Funcionario
from ausencias.models import Ausencia
from .forms import FuncionarioForm, FuncionarioFormUpdate
import datetime


# Create your views here.
@method_decorator(login_required(), name='dispatch')
class FuncionarioList(ListView):
    model = Funcionario


@method_decorator(login_required(), name='dispatch')
class FuncionarioDetail(DetailView):
    model = Funcionario

    def get_context_data(self, **kwargs):
        context = super(FuncionarioDetail, self).get_context_data(**kwargs)
        ausencia_listado = Ausencia.objects.filter(funcionario_id=self.object.id)
        context['ausencia_listado'] = ausencia_listado
        funcionario = Funcionario.objects.get(id=self.object.id)
        # OBTENER EL AÑO ACTUAL.
        hoy = datetime.datetime.now()
        annio = hoy.year

        # CÁLCULO DE FERIADOS LEGALES.
        dias_feriados = 0
        cantidad_feriados = Ausencia.objects.filter(funcionario_id=self.object.id).filter(tipo='FL').filter(
            fecha_inicio__year=annio)
        for cf in cantidad_feriados:
            dias_feriados = dias_feriados + cf.dias
        context['feriados_usados'] = dias_feriados
        feriados_restantes = funcionario.feridos_legales - dias_feriados
        if feriados_restantes <= 0:
            feriados_restantes = 0
        context['feriados_restantes'] = feriados_restantes

        # CÁLCULO DE DIAS ADMINISTRATIVOS.
        dias_administrativos = 0
        cantidad_administrativos = Ausencia.objects.filter(funcionario_id=self.object.id).filter(tipo='AD').filter(
            fecha_inicio__year=annio)
        for ca in cantidad_administrativos:
            dias_administrativos = dias_administrativos + ca.dias
        context['administrativos_usados'] = dias_administrativos
        administrativos_restantes = funcionario.dias_administrativos - dias_administrativos
        if administrativos_restantes <= 0:
            administrativos_restantes = 0
        context['administrativos_restantes'] = administrativos_restantes

        # NOMBRE COMPLETO.
        nombre_completo = funcionario.nombres + ' ' + funcionario.apellido_paterno
        if funcionario.apellido_materno != '':
            nombre_completo = nombre_completo + ' ' + funcionario.apellido_materno
        context['nombre_completo'] = nombre_completo

        return context


# CREAR FUNCIONARIO
@method_decorator(login_required(), name='dispatch')
class FuncionarioCreate(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('funcionarios:funcionarios')


# ACTUALIZAR DATOS DE FUNCIONARIO
@method_decorator(login_required(), name='dispatch')
class FuncionarioUpdate(UpdateView):
    model = Funcionario
    form_class = FuncionarioFormUpdate
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('funcionarios:funcionarios')


# BORRAR UN FUNCIONARIO
@method_decorator(login_required(), name='dispatch')
class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:funcionarios')
