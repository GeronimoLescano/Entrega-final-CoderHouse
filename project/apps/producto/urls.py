from django.urls import path

from .views import *
app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("producto/list/", ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("producto/update/<int:pk>/", ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("producto/delete/<int:pk>/", ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
    path("producto/form/", ProductoCategoriaCreate.as_view(), name="productocategoria_form"),
    path("producto/detail/<int:pk>/", ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path('libros/', libro_list, name='libro_list'),
    path('libros/<int:libro_id>/descargar/', descargar_pdf, name='descargar_pdf'),
]
