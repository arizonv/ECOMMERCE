from django.contrib import messages
from django.utils.html import escape

class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carrito = self.session.get("carrito", {})

    LIMITE_PRODUCTOS = 4

    def agregar(self, producto, cantidad):
        id = str(producto.id)
        if id not in self.carrito:
            # Producto no existe en el carrito
            cantidad_nueva = min(cantidad, producto.stock)
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio_uni": producto.precio,
                "oferta": producto.oferta,
                "acumulado": producto.precio_descuento * cantidad_nueva if producto.oferta != '0' else producto.precio * cantidad_nueva,  # Utilizar el precio con descuento o sin descuento
                "cantidad": cantidad_nueva,
                "stock": producto.stock - cantidad_nueva,
            }
        else:
            # Producto ya existe en el carrito
            cantidad_actual = self.carrito[id]["cantidad"]
            cantidad_total = cantidad_actual + cantidad
            if cantidad_total > self.LIMITE_PRODUCTOS:
                cantidad_nueva = self.LIMITE_PRODUCTOS - cantidad_actual
                mensaje = f"Solo se pueden agregar {self.LIMITE_PRODUCTOS} unidades del producto '{escape(producto.nombre)}' al carrito."
                messages.info(self.request, mensaje)
            else:
                cantidad_nueva = min(cantidad_total, producto.stock) - cantidad_actual
            self.carrito[id]["cantidad"] += cantidad_nueva
            self.carrito[id]["acumulado"] += producto.precio_descuento * cantidad_nueva if producto.oferta != '0' else producto.precio * cantidad_nueva
            self.carrito[id]["stock"] = max(producto.stock - self.carrito[id]["cantidad"], 0)
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            self.carrito[id]["cantidad"] -= 1
            if producto.oferta != '0':
                self.carrito[id]["acumulado"] -= producto.precio_descuento
            else:
                self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
