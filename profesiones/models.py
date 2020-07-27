from django.db import models


# Modelo de Profesión
class Profesion(models.Model):
    nombre = models.CharField(verbose_name="nombre", max_length=50)
    CATEGORIA_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('-'), ('-'),
    )
    categoria = models.CharField(verbose_name="Categoria", max_length=1, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Profesion"
        verbose_name_plural = "profesiones"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


