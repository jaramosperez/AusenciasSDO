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


