from Modelo.Federacion import Federacion
from Utilidades.Utilidades import Utilidades

federacion= Federacion()
def menu():
    salir=False
    print("#################################")
    print("######## MENU PRINCIPAL #########")
    print("#################################")
    print("1 Nueva Liga")
    print("2 Baja Liga")
    print("3 Ver Ligas")
    print("4 Menu Liga")
    print("9 Salir")

    opcion= Utilidades.leerString("Escoge una opción: ")

    if opcion=="1":
        federacion.altaLiga()
        print("1")
    elif opcion=="2":
        federacion.bajaLiga()
        print("2")
    elif opcion=="3":
        federacion.verLigas()
        print("3")
    elif opcion=="4":
        #federacion.login()
        print("4")
    elif opcion=="9":
        print("Saliendo...")
        salir=True
    else:
        print("Escoge una opción válida")
    
    return salir

def app():
    salir=False
    while salir==False:
        salir=menu()

app()
