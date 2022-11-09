from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
        LoginRequiredMixin,
        UserPassesTestMixin
    )
from .models import Articulo

# Create your views here.
class VistaListaArticulos(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    #en vez de mostrar un error, manda a la página de inicio de sesión
    login_url = 'login'

class VistaDetalleArticulo(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'
    login_url = 'login'

class VistaEditarArticulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'cuerpo')
    template_name = 'editar_articulo.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class VistaEliminarArticulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('lista_articulos')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class VistaCrearArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = ('titulo', 'cuerpo')
    login_url = 'login'

    #método para decirle a django quién es el autor del artículo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)