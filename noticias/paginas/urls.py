#./paginas/urls.py
from django.urls import path
from .views import VistaPaginaInicio

urlpatterns = [
    #raiz de app
    path('', VistaPaginaInicio.as_view(), name='inicio'),
]