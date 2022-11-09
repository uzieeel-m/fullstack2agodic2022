from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class PruebasPaginaInicio(SimpleTestCase):
    
    def test_codigo_estado_pagina_inicio(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_vista_url_por_nombre(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)

    def test_vista_usa_plantilla_correcta(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'inicio.html')

class PruebasPaginaRegistro(TestCase):
    nombreusuario = 'nuevousuario'
    email = 'nuevousuario@email.com'

    def test_codigo_estado_registro(self):
        respuesta = self.client.get('/cuentas/registro/')
        self.assertEqual(respuesta.status_code, 200)
    
    def test_url_vista_por_nombre(self):
        respuesta = self.client.get(reverse('signup'))
        self.assertEqual(respuesta.status_code, 200)

    def test_vista_usa_plantilla_correcta(self):
        respuesta = self.client.get(reverse('signup'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'registration/signup.html')

    def test_formulario_registro(self):
        nuevo_usuario = get_user_model().objects.create_user(
            self.nombreusuario, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.nombreusuario)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)