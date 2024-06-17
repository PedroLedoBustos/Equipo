from Modelo.Entrenador import Entrenador
from Modelo.Jugador import Jugador
from Utilidades.Utilidades import Utilidades


class Equipo:
    def __init__(self, nombre, ciudad):
        self.nombre= nombre
        self.ciudad= ciudad
        self.entrenador= None
        self.plantilla= []
        self.jugadorAlto= None

    def getNombre(self):
        return self.nombre

    def getEntrenador(self):
        return self.entrenador
    
    def getJugadorAlto(self):
        return self.jugadorAlto

    def altaEntrenador(self):
        nombre= Utilidades.leerString("Introduce el nombre del entrenador: ")
        apellido= Utilidades.leerString("Introduce el apellido del entrenador: ")
        anioLicencia= Utilidades.leerInteger("Introduce el año de licencia del entrenador: ")

        self.entrenador= Entrenador(nombre,apellido,anioLicencia)

    def altaPlantilla(self):
        numeroJugadores= Utilidades.leerInteger("Introduce el numero de jugadores que quieres en tu equipo: ")
        for n in range(numeroJugadores):
            nombre= Utilidades.leerString("Introduce nombre jugador: ")
            apellido= Utilidades.leerString("Introduce apellido jugador: ")
            dorsal= Utilidades.leerInteger("Introduce dorsal jugador: ")
            altura= Utilidades.leerFloat("Introduce la altura del jugador: ")
            peso= Utilidades.leerFloat("Introduce el peso del jugador: ")

            jugador= Jugador(nombre,apellido,dorsal,altura,peso)

            if any(player.getDorsal() == jugador.getDorsal() for player in self.plantilla):
                print(f"Lo siento, el dorsal {jugador.getDorsal()} ya está asignado.")
            else:
                self.plantilla.append(jugador)
    
    def verJugadorAlto(self):
        jugadorAlto= self.plantilla[0]
        for jugador in self.plantilla:
            if jugador.getAltura()> jugadorAlto.getAltura():
                jugadorAlto= jugador
        
        return jugadorAlto

        

