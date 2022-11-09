from django.urls import path

from paginas.views import vista_pagina_inicio

urlpatterns = [
    path('', vista_pagina_inicio, name='inicio')
]