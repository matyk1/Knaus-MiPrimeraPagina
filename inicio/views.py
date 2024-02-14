from inicio.models import Empleado
from inicio.forms import FormularioNuevoEmpleado

from django.shortcuts import render, redirect
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html', {})

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
    
    return render(request, 'agregar_empleado.html', {'formulario':formulario})

def mostrar_trabajadores(request):
    empleado = Empleado.objects.all()
    return render(request, 'mostrar_trabajadores.html', {'empleado':empleado})