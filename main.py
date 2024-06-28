from Modelo.Liga import Liga
from Utilidades.Utilidades import Utilidades
from Base_datos.conexion import crearConexion, cerrarConexion

def menu():
    salir=False


    print("###############################")
    print("######## MENU PRINCIPAL #######")
    print("###############################")
    print("1 Crear Nueva Liga")
    print("2 Eliminar Liga")
    print("3 Ver ligas")
    print("4 Acceder a Liga existente")
    print("9 Salir")
    opcion= Utilidades.leerString("Escoge una opción: ")

    if opcion == "1":
        repetir= True
        while repetir :
            try:
                conexion=crearConexion()
                cursor= conexion.cursor()
                nombreLiga= Utilidades.leerString("Introduce el nombre de la nueva Liga: ").upper()
                liga= Liga(nombreLiga)
                name= comprobarLigas(cursor, nombreLiga)

                if (name== 'existe'):
                    print('Lo siento ese nombre de liga ya existe, escoge otro\n')
                else: 
                    liga= Liga(nombreLiga)
                    cursor.execute(f"insert into liga(nombre) values ('{liga.getNombre()}');")
                    conexion.commit()

                    cursor.execute(f"SELECT id FROM liga WHERE nombre='{liga.getNombre()}';")
                    idLiga= cursor.fetchall()
                    liga.setIdLiga(idLiga[0][0])
        
                    cerrarConexion(conexion)
                    print("Liga creada correctamente\n")
                    print(f"Id de la liga es: {liga.getIdLiga()}")
                    repetir= False
            
            except:
                print("Se ha producido un error")
                repetir= False
        
    elif opcion == "2":
        conexion=crearConexion()
        cursor= conexion.cursor()
        idEliminar= Utilidades.leerInteger('Introduce el id de la liga que quieres eliminar: ')
        try:
            cursor.execute(f'DELETE FROM liga WHERE id={idEliminar};')
            conexion.commit()

            print(f'La liga con ID= {idEliminar} ha sido eliminada')
            cerrarConexion(conexion)
        except:
            print('Se ha produciro un error al eliminar la liga')
    
    elif opcion == "3":
        conexion=crearConexion()
        cursor= conexion.cursor()
        cursor.execute('SELECT * FROM liga;')
        ligas= cursor.fetchall()
        print("\n------ LISTADO DE LIGAS ------")

        for fila in ligas:
            id= fila[0]
            nombre= fila[1]
            print(f'Número identificador: {id}              Nombre de la liga: {nombre}')
        print()
        
        cerrarConexion(conexion)
    
    elif opcion == "4":
        print("Aun no disponible")

    
    elif opcion == "9":
        print("Saliendo...")
        salir= True
    else:
        print("Opción escogida no válida")
    
    return salir



def aplicacion():
    salir= False
    while salir== False:
        salir= menu()



def comprobarLigas(cursor, nombreNuevo):
    ligasNombre= []
    cursor.execute("SELECT nombre FROM liga;")
    ligas= cursor.fetchall()

    for liga in ligas:
        ligasNombre.append(liga[0])

    for nombre in ligasNombre:
        if nombre.upper()== nombreNuevo.upper():
            return 'existe'
    
    return nombreNuevo.upper()

aplicacion()
    