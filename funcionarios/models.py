from django.db import models
from profesiones.models import Profesion
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class Funcionario(models.Model):
    run = models.CharField(verbose_name="RUN", max_length=9, unique=True)
    nombres = models.CharField(verbose_name="Nombres", max_length=50)
    apellido_paterno = models.CharField(verbose_name="Apellido paterno", max_length=30)
    apellido_materno = models.CharField(verbose_name="Apellido Materno", max_length=30)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True)
    correo = models.EmailField(verbose_name="Correo Electrónico", null=True, blank=True)
    direccion = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    telefono = models.CharField(verbose_name="Número de teléfono", max_length=12, null=True, blank=True)
    anexo = models.PositiveIntegerField(verbose_name="Anexo", null=True, blank=True)
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso", null=True, blank=True)
    fecha_induccion = models.DateField(verbose_name="Fecha de inducción", null=True, blank=True)
    CONTRATO_CHOICES = (
        ('HO', 'HONORARIO'),
        ('CO', 'CONTRATA'),
        ('PL', 'PLANTA'),
        ('EE', 'EXTERNO'),
        ('PP', 'PROGRAMA')
    )
    RELACION_CHOICES = (
        ('PE', 'PERMANENTE'),
        ('TR', 'TRANSITORIO')
    )
    ESTADO_CHOISES = (
        ('VI', 'VINCULADO'),
        ('DV', 'DESVINCULADO')
    )
    contrato = models.CharField(verbose_name="Tipo de contrato", choices=CONTRATO_CHOICES, max_length=2, null=True,
                                blank=True)
    relacion = models.CharField(verbose_name="Tipo de relación", choices=RELACION_CHOICES, max_length=2, null=True,
                                blank=True)
    estado = models.CharField(verbose_name="Estado", choices=ESTADO_CHOISES, max_length=2, null=True, blank=True)
    numero_registro = models.PositiveIntegerField(verbose_name="Número de registro", null=True, blank=True)
    profesion = models.ForeignKey(Profesion, verbose_name="Profesión", on_delete=models.CASCADE)
    dias_administrativos = models.FloatField(verbose_name="Dias administrativos", null=True, blank=True)
    feridos_legales = models.PositiveIntegerField(verbose_name="Feriados Legales", null=True, blank=True)
    foto = models.ImageField(verbose_name="Foto", upload_to="funcionario", null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = ['creado']

    def __str__(self):
        return self.run
