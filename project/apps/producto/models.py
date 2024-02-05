from django.db import models


        
class Libro(models.Model):
    titulo = models.CharField( max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    portada = models.ImageField(upload_to='portadas/')
    pdf = models.FileField(upload_to='pdfs/', default='default.pdf')
    
class DescargaLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_descarga = models.DateTimeField(auto_now_add=True)
    direccion_ip = models.CharField(max_length=100)

    def __str__(self):
        return f'Descarga de {self.libro} el {self.fecha_descarga} desde {self.direccion_ip}'
   