from django.db import models
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    anio_de_empleo = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'