class Producto:

    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        print(f"Nombre {self.nombre}")

class Inventario:

    def __init__(self, Producto):
        self.producto = Producto

    def getProducto(self):
        print(f"Producto, {self.producto}!")
def main():
    producto = Producto("Test")
    inventario = Inventario(producto)