from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['run','nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'correo', 'direccion',
                  'telefono', 'anexo', 'fecha_ingreso', 'fecha_induccion', 'contrato', 'relacion', 'estado',
                  'profesion', 'feridos_legales', 'dias_administrativos', 'numero_registro', 'foto']
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'anexo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'fecha_ingreso': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'fecha_induccion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'contrato': forms.Select(attrs={'class': 'form-control mb-2'}),
            'relacion': forms.Select(attrs={'class': 'form-control mb-2'}),
            'estado': forms.Select(attrs={'class': 'form-control mb-2'}),
            'profesion': forms.Select(attrs={'class': 'form-control mb-2'}),
            'feridos_legales': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'dias_administrativos': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'numero_registro': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'foto': forms.FileInput(attrs={'class': 'form-control mb-2'}),
        }

    def clean_run(self):
        run = self.cleaned_data.get("run")
        if Funcionario.objects.filter(run=run).exists():
            raise forms.ValidationError("El RUN ya esta registrado en la Base de Datos")
        return run

class FuncionarioFormUpdate(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['run','nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'correo', 'direccion',
                  'telefono', 'anexo', 'fecha_ingreso', 'fecha_induccion', 'contrato', 'relacion', 'estado',
                  'profesion', 'feridos_legales', 'dias_administrativos', 'numero_registro', 'foto']
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-2'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'anexo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'fecha_ingreso': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-2'}),
            'fecha_induccion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control mb-2'}),
            'contrato': forms.Select(attrs={'class': 'form-control mb-2'}),
            'relacion': forms.Select(attrs={'class': 'form-control mb-2'}),
            'estado': forms.Select(attrs={'class': 'form-control mb-2'}),
            'profesion': forms.Select(attrs={'class': 'form-control mb-2'}),
            'feridos_legales': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'dias_administrativos': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'numero_registro': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'foto': forms.FileInput(attrs={'class': 'form-control mb-2'}),
        }