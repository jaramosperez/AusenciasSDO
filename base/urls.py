from django.contrib import admin
from django.urls import path
from .views import InicioPageView
urlpatterns = [
    path('', InicioPageView.as_view(), name="inicio"),
]
