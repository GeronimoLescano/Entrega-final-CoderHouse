from django.contrib import admin
from .models import Suscriptor
admin.site.site_title = "Suscripciones"

class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ("email", "fecha_registro")
    
admin.site.register(Suscriptor, SuscriptorAdmin)
