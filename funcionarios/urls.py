from django.urls import path
from .views import FuncionarioList, FuncionarioDetail, FuncionarioCreate, FuncionarioUpdate, FuncionarioDelete

funcionarios_patterns = ([
    path('', FuncionarioList.as_view(), name="funcionarios"),
    path('<int:pk>/<slug:slug>/', FuncionarioDetail.as_view(), name="funcionario"),
    path('crear/', FuncionarioCreate.as_view(), name="crear"),
    path('actualizar/<int:pk>/<slug:slug>/', FuncionarioUpdate.as_view(), name='actualizar'),
    path('borrar/<int:pk>/', FuncionarioDelete.as_view(), name="borrar")
], 'funcionarios')
