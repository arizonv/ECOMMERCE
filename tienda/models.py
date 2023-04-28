from distutils.command import upload
from pyexpat import model
from django.db import models


class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipoAnimal = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    stock = models.IntegerField(null=True, default=0)
    oferta = models.BooleanField()
    imagen = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    numero = models.CharField(max_length=12)
    descripcion = models.TextField(max_length=150)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre




    






