from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
# Create your views here.
from .Carrito import Carrito
from tienda.models import Categorias, Marca, Producto


# def agregar_producto(request, producto_id):
#     carrito = Carrito(request)
#     producto = Producto.objects.get(id=producto_id)
#     cantidad = int(request.POST['cantidad'])
#     carrito.agregar(producto, cantidad)
#     return redirect(reverse("tienda:store"))


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1 # Si no se envió cantidad en el POST, se asigna 1 por defecto
    carrito.agregar(producto, cantidad)
    return redirect(reverse("tienda:store"))



def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect(reverse("tienda:store"))

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect(reverse("tienda:store"))

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(reverse("tienda:store"))