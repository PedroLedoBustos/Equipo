from Modelo.Equipo import Equipo
from Utilidades.Utilidades import Utilidades


class Liga:   
    equipos= []
    entrenadores = []
    jugadoresAltos= []

    def altaEquipo():
        nombre= Utilidades.leerString("Introduce el nombre del equipo: ")
        ciudad= Utilidades.leerString("Introduce la ciudad del equipo: ")

        equipo= Equipo(nombre,ciudad)

        if any(team.getNombre()== equipo.getNombre() for team in Liga.equipos):
            print("Lo siento pero el equipo ya existe")
        else:
            equipo.altaEntrenador()
            equipo.altaPlantilla()
            Liga.equipos.append(equipo)
            print("Equipo dado de alta correctamente")
    
    def bajaEquipo():
        nombre= Utilidades.leerString("Introduce el nombre del equipo que quieres dar de baja: ")
        equipoEncontrado= None

        for team in Liga.equipos:
            if team.getNombre() == nombre:
                equipoEncontrado=team

        if equipoEncontrado:
            Liga.equipos.remove(equipoEncontrado)
            print("Equipo dado de baja correctamente")
        else:
            print("No hay ningun equipo con ese nombre")

    def playerAltos():
        Liga.jugadoresAltos=[]
        for equipo in Liga.equipos:
            jugadorAlto= equipo.verJugadorAlto()
            Liga.jugadoresAltos.append(jugadorAlto)
        
        for jugador in Liga.jugadoresAltos:
            print(f"Nombre: {jugador.getNombre()} Altura: {jugador.getAltura()}")
