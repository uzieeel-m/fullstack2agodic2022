from django.views.generic import TemplateView

# Create your views here.
class VistaPaginaInicio(TemplateView):
    #nombre del archivo html de la plantilla
    template_name = 'inicio.html'