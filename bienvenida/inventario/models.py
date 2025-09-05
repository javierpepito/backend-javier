from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(100)
    precio = models.DecimalField(decimal_places=2)
    stock = models.IntegerField(default=0)
