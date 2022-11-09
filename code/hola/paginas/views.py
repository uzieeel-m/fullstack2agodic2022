from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vista_pagina_inicio(request):
    return HttpResponse('¡Hola mundo!')