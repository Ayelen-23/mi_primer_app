from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length= 50)
    continente = models.CharField(max_length= 30)
    capital =models.CharField(max_length= 50)
    

    def __str__ (self):
        return self.nombre
    

class Organismos(models.Model):
    nombre = models.CharField (max_length= 300)
    descripcion = models.TextField()
    paises_miembros = models.ManyToManyField(Pais, related_name = "organismos")
    
    def __str__ (self):
        return self.nombre
    


