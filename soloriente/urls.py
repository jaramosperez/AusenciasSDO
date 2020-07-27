"""soloriente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from funcionarios.urls import funcionarios_patterns
from ausencias.urls import ausencias_patterns
from reportes.urls import reportes_patterns

urlpatterns = [
    path('', include('base.urls')),
    path('funcionarios/', include(funcionarios_patterns)),
    path('ausencias/', include(ausencias_patterns)),
    path('reportes/', include(reportes_patterns)),
    path('admin/', admin.site.urls),
    # PATH de AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]
