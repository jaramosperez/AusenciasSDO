from django.db import models
from funcionarios.models import Funcionario

# Create your models here.
class Ausencia(models.Model):
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_termino = models.DateField(verbose_name="Fecha de Término")
    funcionario = models.ForeignKey(Funcionario, verbose_name="Funcionario", on_delete=models.CASCADE)
    TIPO_CHOICES = (
        ('FL', 'FERIADO LEGAL'),
        ('AD', 'ADMINISTRATIVO'),
        ('LM', 'LICENCIA MÉDICA'),
        ('CF', 'COMETIDO FUNCIONARIO')
    )
    tipo = models.CharField(verbose_name="Tipo Ausencia", choices=TIPO_CHOICES, max_length=2)
    dias = models.FloatField(verbose_name="Cantidad de dias")
    observacion = models.TextField(verbose_name="Observación", null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Ausencia"
        verbose_name_plural = "Ausencias"
        ordering = ['-fecha_inicio']