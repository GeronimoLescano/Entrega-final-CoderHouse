from django.contrib import admin
from .models import Libro   

admin.site.site_title = "Productos"



class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'portada', 'pdf')
    
    
admin.site.register(Libro, LibroAdmin)



