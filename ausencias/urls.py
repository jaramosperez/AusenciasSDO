from django.urls import path
from .views import AusenciaList, AusenciaDetail, AusenciaCreate, AusenciaUpdate, AusenciaDelete

ausencias_patterns = ([
    path('', AusenciaList.as_view(), name="ausencias"),
    path('<int:pk>/', AusenciaDetail.as_view(), name="ausencia"),
    path('crear/<funcionario_id>', AusenciaCreate.as_view(), name="crear"),
    path('actualizar/<int:pk>/', AusenciaUpdate.as_view(), name="actualizar"),
    path('borrar/<int:pk>/', AusenciaDelete.as_view(), name="borrar")
], 'ausencias')
