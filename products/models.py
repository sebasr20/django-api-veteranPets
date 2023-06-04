from django.db import models
from uuid import uuid4
import os

def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]  # Obtener la extensión del archivo
    filename = f'{uuid4()}.{ext}'  # Generar un nombre único utilizando uuid4()
    return os.path.join('productos', filename)  # Ruta relativa dentro de 'media'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    sigla = models.CharField(max_length=10, default='aaa')
    
    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    serie = models.CharField(max_length=100, null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250, null=False, blank=False)
    codigo = models.CharField(max_length=150)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.DecimalField(max_digits=9, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=get_image_filename, null=True, blank=True)

    def __str__(self):
        return self.nombre