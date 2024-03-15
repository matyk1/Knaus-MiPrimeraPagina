from django.urls import path
from producto import views

urlpatterns = [
    path('juegos/', views.Juegos.as_view(), name='juegos'),
    path('juegos/nuevo/', views.AgregarJuego.as_view(), name='agregar_juego'),
    path('juegos/<int:pk>/eliminar/', views.EliminarJuego.as_view(), name='eliminar_juego'),
    path('juegos/<int:pk>/editar/', views.EditarJuego.as_view(), name='editar_juego'),
    path('juegos/<int:pk>/detalle/', views.DetalleJuego.as_view(), name='detalle_juego'),
]