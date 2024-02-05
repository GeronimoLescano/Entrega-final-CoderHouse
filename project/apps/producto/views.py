from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin





def index(request):
    return render(request, "producto/index.html")

def descargalibro_list(request):
    # Obtener todas las descargas de libros desde la base de datos
    descargas = DescargaLibro.objects.all()
    libro = Libro.objects.all()
    # Renderizar el template 'registro_descargas.html' con los datos de las descargas
    return render(request, 'producto/descargalibro_list.html', {'descargas': descargas, 'libros': libro})




class LibroCreate(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy("producto:libro_list")
    def form_valid(self, form):
        print("Formulario válido")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Formulario inválido")
        print(form.errors)
        return super().form_invalid(form) 
 
class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'producto/libroedit_list.html'
    context_object_name = 'libros'

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ['titulo', 'descripcion', 'portada', 'pdf']
    template_name = 'producto/libroupdate.html'
    success_url = reverse_lazy('producto:libroedit_list')

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('producto:libroedit_list')
    template_name = 'producto/libro_confirm_delete.html'


    
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'producto/libro_list.html', {'libros': libros})







def descargar_pdf(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)

    # Obtener el archivo PDF asociado al libro
    archivo_pdf = libro.pdf

    # Devolver el archivo PDF como una respuesta de archivo
    return FileResponse(archivo_pdf, as_attachment=True, filename="{}.pdf".format(libro.titulo))


    
