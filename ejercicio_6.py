class Producto:

    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        print(f"Nombre {self.nombre}")

class Inventario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def add_producto(self, producto):
        self.productos.append(producto)
    def delete_producto(self, producto):
        self.productos.remove(producto)
    def get_inventario(self):
        print(f"Inventario, {self.nombre}!")
        i=1
        for producto in self.productos:
            print(f"Posición: ", i)
            print(f"Producto:{producto.nombre}")
            i=i+1
def main():
    producto1 = Producto("PC")
    producto2 = Producto("Impresora")
    producto3 = Producto("TV")

    inventario = Inventario("Inventario JNC")
    print("Inventario Inicial")
    inventario.get_inventario()
    inventario.add_producto(producto1)
    inventario.add_producto(producto2)
    inventario.add_producto(producto3)
    print("Carga inicial")
    inventario.get_inventario()
    print("Eliminar un elemento")
    inventario.delete_producto(producto2)
    inventario.get_inventario()
