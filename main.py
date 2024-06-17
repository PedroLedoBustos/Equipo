def menu():
    salir=False
    print("###############################")
    print("######## MENU PRINCIPAL #######")
    print("###############################")
    print("1 Alta Equipo")
    print("2 Alta Equipo")
    print("3 Ver jugadores mas altos")
    print("4 Lista entrenadores ordenada por antiguedad")
    opcion= input("Elige una opción: ")

    if opcion == "1":
        liga.altaEquipo()
    elif opcion == "2":
        liga.bajaEquipo()
    elif opcion == "3":
        liga.verJugadoresAltos()
    elif opcion == "4":
        liga.verEntrenadores()
    elif opcion == "5":
        salir= True
    else:
        print("Opción escogida no válida")
    
    return salir

def aplicacion():
    salir= False
    while salir== False:
        salir= menu()


aplicacion()         