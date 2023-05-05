class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
    # def agregar(self, producto):
    #     id = str(producto.id)
    #     if id not in self.carrito.keys():
    #         self.carrito[id]={
    #             "producto_id": producto.id,
    #             "nombre": producto.nombre,
    #             "precio_uni":producto.precio,
    #             "acumulado": producto.precio_descuento, # Utilizar el precio con descuento
    #             "cantidad": 1,
    #         }
    #     else:
    #         self.carrito[id]["cantidad"] += 1
    #         self.carrito[id]["acumulado"] += producto.precio_descuento # Utilizar el precio con descuento
    #     self.guardar_carrito()

    def agregar(self, producto, cantidad):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio_uni": producto.precio,
                "acumulado": producto.precio_descuento * cantidad if producto.oferta != '0' else producto.precio * cantidad, # Utilizar el precio con descuento o sin descuento
                "cantidad": cantidad,
                "stock": producto.stock - cantidad,
            }
        else:
            self.carrito[id]["cantidad"] += cantidad
            self.carrito[id]["acumulado"] += producto.precio_descuento * cantidad if producto.oferta != '0' else producto.precio * cantidad # Utilizar el precio con descuento o sin descuento
        # Actualizar el stock restante del producto
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
        if id in self.carrito.keys():
            print("okk")
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