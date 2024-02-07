from django.shortcuts import render
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


    
