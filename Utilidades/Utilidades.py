class Utilidades:

    @staticmethod
    def leerString(dato):
        respuesta= input(dato)
        return respuesta
    
    @staticmethod
    def leerInteger(dato):
        while True:
            try:
                respuesta= int(input(dato))
                return respuesta
            except:
                print("Introduce un valor válido")
                
    @staticmethod
    def leerFloat(dato):
        while True:
            try:
                respuesta= float(input(dato))
                return respuesta
            except:
                print("Introduce un valor válido")