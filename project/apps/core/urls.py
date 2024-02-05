from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views
app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path('suscribir/', views.suscribir, name='suscribir'),
    path('suscripcion-exitosa/', views.suscripcion_exitosa_list, name='suscripcion_exitosa_list'),
    path('ya_registrado/', views.ya_registrado_list, name='ya_registrado_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path('register/', register, name='register'),
    ]
