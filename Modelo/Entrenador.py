from Modelo.Persona import Persona


class Entrenador (Persona):
    def __init__(self, nombre, apellido, anioLicencia):
        super().__init__(nombre, apellido)
        self.anioLicencia= anioLicencia
        self.id= None

    
    def getAnioLicencia(self):
        return self.anioLicencia
    
    def setIdEntrenador(self, id):
        self.id= id
    
    def getIdEntrenador(self):
        return self.id