from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('empleado/', views.empleados, name='empleados'),
    path('empleado/nuevo/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/<int:id_empleado>/ver/', views.ver_empleado, name='ver_empleado'),
    path('empleado/<int:id_empleado>/eliminar/', views.eliminar_empleado, name='eleminar_empleado'),
    path('empleado/<int:id_empleado>/editar/', views.editar_empleado, name='editar_empleado'),
    path('about_me/', views.about_me, name='about_me')
]
