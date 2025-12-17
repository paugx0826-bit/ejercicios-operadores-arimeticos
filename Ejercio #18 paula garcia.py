import math

def capturar_datos():
    lado = float(input("ingrese el lado del hexágono: "))
    return lado

def procesar(lado):
    area = (3 * math.sqrt(3) / 2) * (lado ** 2)
    return area

def mostrar(area):
    print("el área del hexágono regular es:", area)

lado = capturar_datos()
area = procesar(lado)
mostrar(area)
