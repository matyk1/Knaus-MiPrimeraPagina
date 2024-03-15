from inicio.models import Empleado
from inicio.forms import FormularioNuevoEmpleado, FormularioBusquedaEmpleado, FormularioEdicionEmpleado

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def empleados(request): 
    formulario = FormularioBusquedaEmpleado(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        empleado = Empleado.objects.filter(nombre__icontains=nombre_a_buscar) 
    
    return render(request, 'inicio/empleados.html', {'empleados':empleado, 'formulario':formulario})

@login_required
def agregar_empleado(request):
    formulario = FormularioNuevoEmpleado()
    if request.method =='POST':
        formulario = FormularioNuevoEmpleado(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            edad = formulario.cleaned_data.get('edad')
            anio_de_empleo = formulario.cleaned_data.get('anio_de_empleo')
            empleado = Empleado(nombre=nombre, apellido=apellido, edad=edad, anio_de_empleo=anio_de_empleo)
            empleado.save()
        return redirect('agregar_empleado')
    
    return render(request, 'inicio/agregar_empleado.html', {'formulario':formulario})

@login_required
def eliminar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()
    
    return redirect('empleados')

@login_required
def editar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    formulario = FormularioEdicionEmpleado(initial={'nombre':empleado.nombre, 'apellido':empleado.apellido, 'edad':empleado.edad, 'anio_de_empleo':empleado.anio_de_empleo})
    if request.method =='POST':
        formulario = FormularioEdicionEmpleado(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            empleado.nombre = info_nueva.get('nombre')
            empleado.apellido = info_nueva.get('apellido')
            empleado.edad = info_nueva.get('edad')
            empleado.anio_de_empleo = info_nueva.get('anio_de_empleo')
            empleado.save()
            return redirect('empleados')
    
    return render(request, 'inicio/editar_empleado.html', {'empleado': empleado, 'formulario':formulario})
    
def ver_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    
    return render(request, 'inicio/ver_empleado.html', {'empleado': empleado})

def about_me(request):
    return render(request, 'inicio/about_me.html', {})