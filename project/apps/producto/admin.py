from django.contrib import admin
from .models import Libro, DescargaLibro

admin.site.site_title = "Productos"


class DescargaLibroAdmin(admin.ModelAdmin):
    list_display = ('libro', 'fecha_descarga', 'direccion_ip')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'portada', 'pdf')
    
    
admin.site.register(Libro, LibroAdmin)
admin.site.register(DescargaLibro, DescargaLibroAdmin)


