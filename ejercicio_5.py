def main():
    try:
        resultado = 15 + "20"
        print(resultado)
    except TypeError:
        print("No puede sumar dos valores con diferente tipo de valor. 'int' y 'str' son los valores utilizados")
    finally:
        print("Operación finalizada.")
