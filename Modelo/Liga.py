from Modelo.Equipo import Equipo
from Utilidades.Utilidades import Utilidades


class Liga:
    def __init__(self, nombre):
        self.nombre= nombre   
        self.equipos= []
        self.entrenadores = []
        self.jugadoresAltos= []
        self.id= None
    
    def getNombre(self):
        return self.nombre
    
    def setIdLiga(self, id):
        self.id= id

    def getIdLiga(self):
        return self.id

    def altaEquipo(self):
        nombre= Utilidades.leerString("Introduce el nombre del equipo: ")
        ciudad= Utilidades.leerString("Introduce la ciudad del equipo: ")

        equipo= Equipo(nombre,ciudad)

        if any(team.getNombre()== equipo.getNombre() for team in self.equipos):
            print("Lo siento pero el equipo ya existe")
        else:
            equipo.altaEntrenador()
            equipo.altaPlantilla()
            self.equipos.append(equipo)
            print("Equipo dado de alta correctamente")
    
    def bajaEquipo(self):
        nombre= Utilidades.leerString("Introduce el nombre del equipo que quieres dar de baja: ")
        equipoEncontrado= None

        for team in self.equipos:
            if team.getNombre() == nombre:
                equipoEncontrado=team

        if equipoEncontrado:
            self.equipos.remove(equipoEncontrado)
            print("Equipo dado de baja correctamente")
        else:
            print("No hay ningun equipo con ese nombre")

    def playerAltos(self):
        self.jugadoresAltos=[]
        for equipo in self.equipos:
            jugadorAlto= equipo.verJugadorAlto()
            if jugadorAlto != None:
                self.jugadoresAltos.append(jugadorAlto)
        
        if not self.jugadoresAltos:
            print("No hay jugadores registrados")
        else:
            for jugador in self.jugadoresAltos:
                print(f"Nombre: {jugador.getNombre()} Altura: {jugador.getAltura()}")

    def entrenadoresOrdenados(self):
        self.entrenadores=[]

        for equipo in self.equipos:
            entrenador= equipo.getEntrenador()
            self.entrenadores.append(entrenador)
        
        self.entrenadores.sort(key=lambda entrenador: entrenador.getAnioLicencia())

        for mister in self.entrenadores:
            print(f"Nombre: {mister.getNombre()} Año Licencia: {mister.getAnioLicencia()}")












'''
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
'''

