from Modelo.Persona import Persona


class Entrenador (Persona):
    def __init__(self, nombre, apellido, anioLicencia):
        super().__init__(nombre, apellido)
        self.anioLicencia= anioLicencia

    
    def getAnioLicencia(self):
        return self.anioLicencia