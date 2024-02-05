from django import forms
from .models import *




class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['portada'].widget.attrs.update({'accept': 'image/*'})