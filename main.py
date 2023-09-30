import ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("-----Menu-----")
    print("1 - Ejercicio 1")
    print("2 - Ejercicio 2")
    print("3 - Ejercicio 3")
    print("4 - Ejercicio 4")
    print("5 - Ejercicio 5")
    print("6 - Ejercicio 6")
    menu = int(input())
    match menu:
        case 1:
            ejercicio_1.main()
        case 2:
            ejercicio_2.main()
        case 3:
            ejercicio_3.main()
        case 4:
            ejercicio_4.main()
        case 5:
            ejercicio_5.main()
        case 6:
            ejercicio_6.main()
        case default:
            print("El numero no se encuentra en la lista")

