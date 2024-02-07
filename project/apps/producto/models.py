from django.db import models


        
class Libro(models.Model):
    titulo = models.CharField( max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    portada = models.ImageField(upload_to='portadas/')
    pdf = models.FileField(upload_to='pdfs/', default='default.pdf')
    

