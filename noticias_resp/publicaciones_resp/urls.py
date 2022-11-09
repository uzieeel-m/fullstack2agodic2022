#publicaciones/urls.py
#este archivo contiene las urls del modulo publicaciones
from django.urls import path
from .views import VistaPaginaInicio

urlpatterns = [
    #establecer la raíz del modulo
    path('', VistaPaginaInicio.as_view(), name='inicio'),
]