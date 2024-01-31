from django import forms
from .models import *


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        fields = "__all__"
