"""Estadisticas descriptivas basicas sobre una lista de datos."""

datos = [10, 25, 13, 8, 42, 17, 25, 31]


def media(valores):
    return sum(valores) / len(valores)


def mediana(valores):
    ordenados = sorted(valores)
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (ordenados[medio - 1] + ordenados[medio]) / 2
    return ordenados[medio]


def varianza(valores):
    m = media(valores)
    return sum((v - m) ** 2 for v in valores) / len(valores)


def desviacion_estandar(valores):
    return varianza(valores) ** 0.5


if __name__ == "__main__":
    print("Datos:", datos)
    print("Media:", round(media(datos), 2))
    print("Mediana:", mediana(datos))
    print("Varianza:", round(varianza(datos), 2))
    print("Desviacion estandar:", round(desviacion_estandar(datos), 2))
