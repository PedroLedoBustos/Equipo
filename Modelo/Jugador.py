from Modelo.Persona import Persona


class Jugador (Persona):
    def __init__(self, nombre, apellido, dorsal, altura, peso):
        super().__init__(nombre, apellido)
        self.dorsal= dorsal
        self.altura= altura
        self.peso= peso

    def getDorsal(self):
        return self.dorsal
    
    def getAltura(self):
        return self.altura
    
    def getPeso(self):
        return self.peso