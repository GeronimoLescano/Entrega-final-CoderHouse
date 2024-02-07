from django.urls import path

from .views import *
app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("producto/form/", LibroCreate.as_view(), name="libro_form"),
    path("producto/update/<int:pk>/", LibroUpdateView.as_view(), name="libroupdate"),
    path("producto/delete/<int:pk>/", LibroDeleteView.as_view(), name="libro_confirm_delete"),
    path("producto/list/", LibroListView.as_view(), name="libroedit_list"),
    path('libros/', libro_list, name='libro_list'),
    path('libros/<int:libro_id>/descargar/', descargar_pdf, name='descargar_pdf'),

]
