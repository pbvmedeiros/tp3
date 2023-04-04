from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Tienda(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)