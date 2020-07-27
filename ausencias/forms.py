from django import forms
from .models import Ausencia


class AusenciaForm(forms.ModelForm):

    class Meta:
        model = Ausencia
        fields = ['tipo', 'fecha_inicio', 'fecha_termino', 'dias', 'observacion']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'ui selection dropdown'}),
            'fecha_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui calendar', 'type': 'date', 'id': '#example1'}),
            'fecha_termino': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-1', 'type': 'date'}),
            'dias': forms.NumberInput(attrs={'class': 'ui input error', 'type': 'text'}),
            'observacion': forms.Textarea(attrs={'class': 'ui input'})
        }
