from django.urls import path
from .views import ReporteLicenciasExcelMesActual, \
    ReporteLicenciasExcelMesPasado, \
    ReporteInduccionesExcel, \
    ReporteList, \
    ReporteTotalExcel

reportes_patterns = ([
    path('', ReporteList.as_view(), name= 'reporteList'),
    path('ReportLicenciasExcelMesActual/', ReporteLicenciasExcelMesActual.as_view(), name='ReportLicenciasExcelMesActual'),
    path('ReportLicenciasExcelMesPasado/', ReporteLicenciasExcelMesPasado.as_view(), name='ReportLicenciasExcelMesPasado'),
    path('ReporteInduccionesExcel/', ReporteInduccionesExcel.as_view(), name='ReporteInduccionesExcel'),
    path('ReporteTotalExcel/', ReporteTotalExcel.as_view(), name='ReporteTotalExcel')
], 'reportes')