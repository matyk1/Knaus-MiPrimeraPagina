from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('empleado/', empleados, name='empleados'),
    path('empleado/nuevo/', agregar_empleado, name='agregar_empleado'),
    path('empleado/<int:id_empleado>/ver/', ver_empleado, name='ver_empleado'),
    path('empleado/<int:id_empleado>/eliminar/', eliminar_empleado, name='eleminar_empleado'),
    path('empleado/<int:id_empleado>/editar/', editar_empleado, name='editar_empleado'),
]
