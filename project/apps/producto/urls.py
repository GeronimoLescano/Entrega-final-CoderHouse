from django.urls import path

from .views import *
app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("producto/form/", LibroCreate.as_view(), name="libro_form"),
    path("producto/update/<int:pk>/", LibroUpdateView.as_view(), name="libroupdate"),
    path("producto/delete/<int:pk>/", LibroDeleteView.as_view(), name="libro_confirm_delete"),
    #path("producto/detail/<int:pk>/", LibroDetailView.as_view(), name="libro_detail"),
    path("producto/list/", LibroListView.as_view(), name="libroedit_list"),
    path('libros/', libro_list, name='libro_list'),
    path('libros/<int:libro_id>/descargar/', descargar_pdf, name='descargar_pdf'),
    path('descargas-libros/', descargalibro_list, name='descargalibro_list'),
    #path('libros/<int:libro_id>/descargar/', DescargarLibroView.as_view(), name='descargar_libro'),
]
