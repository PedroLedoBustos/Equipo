from Modelo.Liga import Liga
from Modelo.Sentencias import Sentencias
from Utilidades.Utilidades import Utilidades


class Federacion:

    def __init__(self):
        pass

    
    def crearLiga(self):
        nLigas= Sentencias.cantidadLigas()
        nombre= Utilidades.leerString("Introduce el nombre de la liga: ").upper()
        id= nLigas + 1
        liga= Liga(id, nombre)
        return liga
    
    def altaLiga(self):
        liga= self.crearLiga()
        Sentencias.altaLigaSql(liga)
    
    def bajaLiga(self):
        liga= self.crearLiga()
        Sentencias.eliminarLiga(liga)

    def verLigas(self):
        Sentencias.verLigasSql()

        


    


        