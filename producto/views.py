from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from producto.models import Juego
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
    
class Juegos(ListView):
    model = Juego
    context_object_name = 'juegos'
    template_name = 'juegos/juegos.html'
    
class AgregarJuego(LoginRequiredMixin, CreateView):
    model = Juego
    template_name = 'juegos/agregar_juego.html'
    fields = ['nombre', 'descripcion', 'consola', 'version', 'fecha_lanzamiento', 'compania']
    success_url = reverse_lazy('juegos')

class EliminarJuego(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = 'juegos/eliminar_juego.html'
    success_url = reverse_lazy('juegos')
    
class EditarJuego(LoginRequiredMixin, UpdateView):
    model = Juego
    template_name = 'juegos/editar_juego.html'
    success_url = reverse_lazy('juegos')
    fields = ['nombre', 'descripcion', 'consola', 'version', 'fecha_lanzamiento', 'compania']
    
class DetalleJuego(DetailView):
    model = Juego
    template_name = "juegos/detalle_juego.html"