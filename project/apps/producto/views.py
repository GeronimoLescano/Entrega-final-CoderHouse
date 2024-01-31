from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from reportlab.pdfgen import canvas
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO


from .forms import *
from .models import *

def index(request):
    return render(request, "producto/index.html")

class ProductoCategoriaList(ListView):
    model = ProductoCategoria
    # template_name = "producto/productocategoria_listXX.html"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = ProductoCategoria.objects.all()
        return object_list

class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
    
class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
    
    
class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    
class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
    
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'producto/libro_list.html', {'libros': libros})

def descargar_pdf(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    buffer = BytesIO()
    
    # Generar PDF con reportlab
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Título: {}".format(libro.titulo))
    # Agregar más contenido al PDF según tus necesidades
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="{}.pdf".format(libro.titulo))
