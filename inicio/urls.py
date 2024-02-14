from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('trabajador/nuevo', agregar_empleado, name='agregar_empleado'),
    path('trabajador/lista', mostrar_trabajadores, name='mostrar_trabajadores'),
]
