from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Ausencia
from .forms import AusenciaForm
from funcionarios.models import Funcionario


# LISTAR LAS AUSENCIAS.
@method_decorator(login_required(), name='dispatch')
class AusenciaList(ListView):
    model = Ausencia


# DETALLE DE AUSENCIA.
@method_decorator(login_required(), name='dispatch')
class AusenciaDetail(DetailView):
    model = Ausencia


# CREAR UNA AUSENCIA PARA UN FUNCIONARIO.
@method_decorator(login_required(), name='dispatch')
class AusenciaCreate(CreateView):
    model = Ausencia
    form_class = AusenciaForm
    success_url = reverse_lazy('ausencias:ausencias')

    # IDENTIFICAR AL FUNCIONARIO AL QUE SE LE AÑADIRÁ LA AUSENCIA.
    def form_valid(self, form):
        funcionario_id = self.kwargs['funcionario_id']
        form.instance.funcionario = Funcionario.objects.get(id=funcionario_id)
        return super(AusenciaCreate, self).form_valid(form)

    # OBTENER LOS DATOS PARA EL FUNCIONARIO SELECCIONADO.
    def get_context_data(self, **kwargs):
        context = super(AusenciaCreate, self).get_context_data(**kwargs)
        funcionario_id = self.kwargs['funcionario_id']
        funcionario = Funcionario.objects.get(id=funcionario_id)
        context['funcionario'] = funcionario
        return context


# ACTUALIZAR LOS DATOS DE UNA AUSENCIA.
@method_decorator(login_required(), name='dispatch')
class AusenciaUpdate(UpdateView):
    model = Ausencia
    form_class = AusenciaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ausencias:actualizar', args=[self.object.id]) + '?ok'


# BORRAR UNA AUSENCIA.
@method_decorator(login_required(), name='dispatch')
class AusenciaDelete(DeleteView):
    model = Ausencia
    success_url = reverse_lazy('ausencias:ausencias')
