from django.db import models

from django.utils import timezone


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"


class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100, verbose_name="unidad de medida")
    cantidad = models.FloatField()
    precio = models.FloatField()
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    def __str__(self) -> str:
        return f"{self.nombre} ${self.precio:.2f}"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        
class Libro(models.Model):
    titulo = models.CharField( max_length=100)
    portada = models.ImageField(upload_to='portadas/')
    pdf = models.FileField(upload_to='pdfs/', default='default.pdf')