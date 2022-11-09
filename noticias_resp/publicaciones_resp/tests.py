from django.test import TestCase
from django.urls import reverse
from .models import Publicaciones

# Create your tests here.
class PruebaModeloPublicaciones(TestCase):

    #método que se ejecuta antes de todas las pruebas, por eso se pone al inicio de la clase
    def setUp(self):
        #insertar en la bd un objeto para hacer pruebas
        Publicaciones.objects.create(texto='solo una prueba')

    def test_contenido_texto(self):
        #crea una copia de la bd para hacer pruebas
        #obtiene el objeto que se creó en en setUp
        pub = Publicaciones.objects.get(id=1)
        #para no concatenar el texto a la variable (cosas de python)
        texto_esperado = f'{pub.texto}'
        self.assertEqual(texto_esperado, 'solo una prueba')

class PruebaVistaPaginaInicio(TestCase):

    def setUp(self):
        Publicaciones.objects.create(texto='esto es otra prueba')

    #validar que exista la vista en una url apropiada
    def test_existe_vista_url_apropiada(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_vista_url_por_nombre(self):
        #el metodo reverse convierte nombre de url en una url completa
        resp = self.client.get(reverse('inicio'))
        self.assertEqual(resp.status_code, 200)

    def test_vista_usa_plantilla_correcta(self):
        #obtiene la página inicio
        resp = self.client.get(reverse('inicio'))
        #revisa que exista
        self.assertEqual(resp.status_code, 200)
        #que se esté utilizando la plantilla inicio.html
        self.assertTemplateUsed(resp, 'inicio.html')