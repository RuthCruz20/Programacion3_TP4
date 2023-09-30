def main():
    usuario_info = {
        "nombres": [],
        "edades": [],
        "direcciones": [],
        "telefonos": []
    }
    tamaño = 2
    for i in range(tamaño):
        print("Ingrese los datos de la persona", i + 1)
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")

        usuario_info["nombres"].append(nombre)
        usuario_info["edades"].append(edad)
        usuario_info["direcciones"].append(direccion)
        usuario_info["telefonos"].append(telefono)

    for i in range(tamaño):
        print("Mostrando los datos del usuario", i + 1)

        print("Nombre:", usuario_info["nombres"][i])
        print("Edad:", usuario_info["edades"][i])
        print("Direccion:", usuario_info["direcciones"][i])
        print("Telefono:", usuario_info["telefonos"][i])