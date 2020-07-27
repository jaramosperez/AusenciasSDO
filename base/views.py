from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class InicioPageView(TemplateView):
    template_name = "base/inicio.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'RRHH'})
