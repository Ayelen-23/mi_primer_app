from django.db import models
from datetime import date
# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length= 50)
    continente = models.CharField(max_length= 30)
    capital =models.CharField(max_length= 50)
    

    def __str__ (self):
        return self.nombre
    

class Organismos(models.Model):
    nombre = models.CharField (max_length= 300)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(default=date (2000, 1, 1))
    activo = models.BooleanField(default=True)
    
    def __str__ (self):
        return self.nombre
    
class Acuerdos(models.Model):
    nombre = models.CharField (max_length= 300)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(default=date (2000, 1, 1))
    activo = models.BooleanField(default=True)
    
    def __str__ (self):
        return self.nombre
    


