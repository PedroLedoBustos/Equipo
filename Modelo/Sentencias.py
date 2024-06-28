from Base_datos.conexion import crearConexion, cerrarConexion

class Sentencias:
    def __init__(self):
        pass
    
    @staticmethod
    def cantidadLigas():
        nLigas=0
        try:
            conexion= crearConexion()
            cursor= conexion.cursor()
            cursor.execute(f"SELECT * FROM liga;")
            infoLigas= cursor.fetchall()
            for fila in infoLigas:
                nLigas +=1

            cerrarConexion(conexion)
        except:
            print("Error con la base de datos")
        
        return nLigas
    
    @staticmethod
    def comprobarLiga(liga):
        try:
            conexion= crearConexion()
            cursor= conexion.cursor()
            cursor.execute(f"SELECT * FROM liga;")
            infoLigas= cursor.fetchall()
            for fila in infoLigas:
                if liga.getNombre() == fila[1]:
                    return 'Existe'

            cerrarConexion(conexion)
            return 'No Existe'
        except:
            print("Error con la base de datos")

    @staticmethod
    def altaLigaSql(liga):
        try:
            conexion= crearConexion()
            cursor= conexion.cursor()
            esta= Sentencias.comprobarLiga(liga)
            if esta== 'No Existe':
                cursor.execute(f"INSERT INTO liga(id, nombre) VALUES ({liga.getId()}, '{liga.getNombre()}');")
                conexion.commit()
            else:
                print("Lo siento esa liga ya existe")

            cerrarConexion(conexion)
        except:
            print("Error con la base de datos")
    
    @staticmethod
    def eliminarLiga(liga):
        try:
            conexion= crearConexion()
            cursor= conexion.cursor()
            esta= Sentencias.comprobarLiga(liga)
            if esta== 'Existe':
                cursor.execute(f"DELETE FROM liga WHERE nombre= '{liga.getNombre()}'")
                conexion.commit()
            else:
                print("Lo siento esa liga no existe")
            cerrarConexion(conexion)
        except:
            print("Error con la base de datos")
    
    @staticmethod
    def verLigasSql():
        try:
            conexion= crearConexion()
            cursor= conexion.cursor()
            cursor.execute(f"SELECT * FROM liga;")
            infoLigas= cursor.fetchall()
            print(" ----------- LIGAS -----------")
            for fila in infoLigas:
                print(f'ID: {fila[0]}  Nombre: {fila[1]}')
            cerrarConexion(conexion)
        except:
            print("Error con la base de datos")
    




