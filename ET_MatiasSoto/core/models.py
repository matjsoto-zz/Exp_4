from django.db import models
from django.db.models.deletion import CASCADE

class Persona(models.Model):
    rut = models.CharField(max_length = 12, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length = 100, verbose_name='Nombre')
    telefono = models.CharField(max_length = 9, verbose_name='Telefono')
    direccion = models.CharField(max_length = 100, verbose_name='Direccion')
    email = models.CharField(max_length = 200, verbose_name='Email')
    pais = models.CharField(max_length = 100, verbose_name='Pais')
    contraseña = models.CharField(max_length = 100, verbose_name='Contraseña')

    def __str__(self):

        return (self.rut)