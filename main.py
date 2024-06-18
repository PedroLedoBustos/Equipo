from Modelo.Liga import Liga

liga= Liga()

def menu():
    salir=False
    print("###############################")
    print("######## MENU PRINCIPAL #######")
    print("###############################")
    print("1 Alta Equipo")
    print("2 Baja Equipo")
    print("3 Ver jugadores mas altos")
    print("4 Lista entrenadores ordenada por antiguedad")
    print("5 Salir")
    opcion= input("Elige una opción: ")

    if opcion == "1":
        liga.altaEquipo()
    elif opcion == "2":
        liga.bajaEquipo()
    elif opcion == "3":
        liga.playerAltos()
    elif opcion == "4":
        liga.entrenadoresOrdenados()
    elif opcion == "5":
        print("Saliendo...")
        salir= True
    else:
        print("Opción escogida no válida")
    
    return salir

def aplicacion():
    salir= False
    while salir== False:
        salir= menu()


aplicacion()         