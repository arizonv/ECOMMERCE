import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web.settings')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


import django
django.setup()

from django.contrib.auth.models import User
from django_web import settings
from faker import Faker
from tienda.models import Categorias, Marca, Producto, contacto

fake = Faker()

# Crear categorías
for i in range(5):
    nombre = fake.word()
    categoria = Categorias.objects.create(nombre=nombre)
    categoria.save()

# Crear marcas
for i in range(5):
    nombre = fake.company()
    marca = Marca.objects.create(nombre=nombre)
    marca.save()

# Crear productos
for i in range(10):
    nombre = fake.word()
    precio = fake.random_int(min=10, max=1000)
    descripcion = fake.paragraph()
    marca = Marca.objects.order_by('?').first()
    categoria = Categorias.objects.order_by('?').first()
    stock = fake.random_int(min=0, max=100)
    oferta = fake.random_element(elements=('0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50'))
    nuevo = fake.boolean()
    imagen = r"sqlPoblado/audifonos.jpg"
    producto = Producto.objects.create(nombre=nombre, precio=precio, descripcion=descripcion, marca=marca, categoria=categoria, stock=stock, oferta=oferta, nuevo=nuevo, imagen=imagen)
    producto.save()

# Crear contactos
for i in range(5):
    nombre = fake.first_name()
    apellido = fake.last_name()
    email = fake.email()
    numero = fake.phone_number()
    descripcion = fake.paragraph()
    region = fake.state()
    comuna = fake.city()
    nuevo_contacto = contacto.objects.create(nombre=nombre, apellido=apellido, email=email, numero=numero, descripcion=descripcion, region=region, comuna=comuna)
    nuevo_contacto.save()
