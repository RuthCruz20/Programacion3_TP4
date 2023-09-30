def main():
    print("Ejercicio 1")
    lista_con_numeros = [2, 5, 3]
    encontrado = True
    numero = int(input("Ingresa un numero entre 1 y 9: "))
    while (numero < 0 or numero > 9):
        print("Numero incorrecto")
        numero = float(input('Ingresa un numero entre 1 y 9: '))

    for num in lista_con_numeros:
        if (num == numero):
            encontrado = True
            break
        else:
            encontrado = False
    if (encontrado):
        print("El numero ", numero, "se encuentra en la lista")
    else:
        print("El numero ", numero, "no se encuentra en la lista")