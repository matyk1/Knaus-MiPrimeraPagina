from django import forms

class FormularioBaseEmpleado(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    anio_de_empleo = forms.IntegerField()
    
class FormularioNuevoEmpleado(FormularioBaseEmpleado):
    ...
    
class FormularioEdicionEmpleado(FormularioBaseEmpleado):
    ...
        
class FormularioBusquedaEmpleado(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)