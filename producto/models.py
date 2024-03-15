from django.db import models
    
class Juego(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    consola = models.CharField(max_length=30)
    version = models.FloatField()
    fecha_lanzamiento = models.DateField()
    compania = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} - {self.consola}'