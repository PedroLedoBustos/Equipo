''' Probando Conexion Base de Datos'''
import mysql.connector

def crearConexion():
    conexion = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password= '',
        db= 'liga'
    )
    if (conexion.is_connected()):
        print(f'Conexion a la base de datos realizada con exito')
    else:
        print('Error al conectarse a la base de datos')

    return conexion

def insertarEntrenador():
    conexion= crearConexion()

    cursor= conexion.cursor()

    cursor.execute("insert into entrenadores(id,nombre, apellido, anioLicencia) values (1, 'Pedro', 'Ledo', 2006);")
    conexion.commit()

    cerrarConexion(conexion)

    print("Entrenador insertado con exito")

def cerrarConexion(conexion):
    conexion.close()

    if (conexion.is_connected()):
        print(f'Sigues conectado a la base de datos')
    else:
        print('ya no estas conectado a la base de datos')



insertarEntrenador()

    


