from coordenadas import *


def test_calcular_media_coordenadas():
    """Función para testear media_coordenadas
    """
    print("Test de calcular_media_coordenadas:")
    coordenadas = [
        Coordenadas(36.52016726032299, -6.151330284937666),
        Coordenadas(36.67525095554243, -5.446052739188258),
    ]
    media = calcular_media_coordenadas(coordenadas)
    print(f"La media de las coordenadas de los centros es {media}.")
    print("=======================================================")


def test_calcular_distancia():
    """Función para testear calcular_distancia
    """
    print("Test de calcular_media_coordenadas:")
    coordenada1 = Coordenadas(36.52016726032299, -6.151330284937666)
    coordenada2 = Coordenadas(36.67525095554243, -5.446052739188258)
    distancia = calcular_distancia(coordenada1, coordenada2)
    print(
        f"La distancia entre las coordenadas {coordenada1} y {coordenada2} es {distancia}"
    )
    print("=======================================================")


if __name__ == "__main__":
    test_calcular_distancia()
    test_calcular_media_coordenadas()

