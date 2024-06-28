from Modelo.Entrenador import Entrenador
from conexion import crearConexion, cerrarConexion


def agregarEntrenador(entrenador):
    conexion= crearConexion()
    cursor= conexion.cursor()

    cursor.execute(f"insert into entrenadores(nombre, apellido, anioLicencia) values ('{entrenador.getNombre()}', '{entrenador.getApellido()}', {entrenador.getAnioLicencia()});")
    conexion.commit()
    cursor.execute(f"SELECT * FROM entrenadores WHERE nombre= '{entrenador.getNombre()}';")
    idEntrenador= cursor.fetchall()
    entrenador.setIdEntrenador(idEntrenador[0])

    print(f"Entrenador agregado correctamente con id = {idEntrenador[0]}")
    cerrarConexion(conexion)


entrenador= Entrenador('Pedro', 'Ledo', 1991)

agregarEntrenador(entrenador)