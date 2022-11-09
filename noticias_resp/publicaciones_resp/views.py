#para poder ver la lista de todas las publicaciones, y no solo una
from django.views.generic import ListView
#desde el archivo models de la carpeta actual, importar Publicaciones
from .models import Publicaciones

# Create your views here.
class VistaPaginaInicio(ListView):
    model = Publicaciones
    template_name = 'inicio.html'
    context_object_name = 'lista_publicaciones'