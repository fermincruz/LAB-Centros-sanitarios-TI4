from centros import *


def test_lee_centros(datos):
    """
    Prueba la función lee_centros
    """
    print("Test de lee_centros:")
    print("Número de registros leídos:", len(datos))
    print("Mostrando los 3 primeros:")
    for c in datos[:3]:
        print("\t", c)
    print("Mostrando los 3 últimos:")
    for c in datos[-3:]:
        print("\t", c)
    print("=======================================================")


if __name__ == "__main__":
    datos = leer_centros("data/centrosSanitarios.csv")
    test_lee_centros(datos)
