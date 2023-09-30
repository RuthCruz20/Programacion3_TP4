def main():
    usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}
    administradores = {"Juan", "Marcela"}
    print("Usuarios:", usuarios)
    print("Administradores:", administradores)
    print("Eliminando a Juan como administrador")
    administradores.discard("Juan")
    print("Usuarios:", usuarios)
    print("Administradores:", administradores)
    print("Agregando a Marco como administrador")
    administradores.add("Marco")
    print("Usuarios:", usuarios)
    print("Administradores:", administradores)