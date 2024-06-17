from Modelo.Equipo import Equipo
from Utilidades.Utilidades import Utilidades


class Liga:

    def __init__(self):
        self.equipos= []
        self.entrenadores = []
        self.jugadoresAltos= []

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
