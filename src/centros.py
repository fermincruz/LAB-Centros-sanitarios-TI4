from collections import namedtuple
from coordenadas import *
import csv

CentroSanitario = namedtuple(
    "CentroSanitario",
    "nombre,localidad, coordenada, estado, num_camas, acceso_minusvalidos, tiene_uci",
)


# TODO: Existen DOS errores en esta implementación. Corrígelos.
def leer_centros(ruta_fichero):
    """
    Lee el fichero de entrada y devuelve una lista de tuplas de tipo CentroSanitario
    
    Parámetros:
        ruta_fichero: ruta del fichero CSV, de tipos str.
    Devuelve:
        lista de tuplas de tipo CentroSanitario
    """
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        centros = []
        for (
            nombre,
            localidad,
            latitud,
            longitud,
            estado,
            num_camas,
            acceso_minusvalidos,
            tiene_uci,
        ) in lector:
            nombre = nombre
            localidad = localidad
            coordenada = Coordenadas(float(latitud), float(longitud))
            num_camas = int(num_camas)
            acceso_minusvalidos = parsea_booleano(acceso_minusvalidos)
            tiene_uci = parsea_booleano(tiene_uci)
            centros.append(
                CentroSanitario(
                    nombre,
                    localidad,
                    coordenada,
                    estado,
                    num_camas,
                    acceso_minusvalidos,
                    tiene_uci,
                )
            )
        return centros


def parsea_booleano(cadena):
    return cadena == "true"


# TODO: Implemente el resto de funciones que se piden en el enunciado