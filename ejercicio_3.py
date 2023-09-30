def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    return [pares, impares]
def main():
    lista = [6,5,2,1,7]
    pares, impares = separar(lista)
    print("Listado: ", lista)
    print("Pares: ", pares)
    print("Impares: ", impares)

