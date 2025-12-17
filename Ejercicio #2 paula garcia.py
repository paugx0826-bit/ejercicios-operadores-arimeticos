import math

def pedir_radio():
    r = float(input("Ingrese el radio de la esfera: "))
    return r

def calcular_volumen(r):
    volumen = (4/3) * math.pi * (r ** 3)
    return volumen

def mostrar_volumen(volumen):
    print("El volumen de la esfera es:", volumen)

# PROGRAMA PRINCIPAL
radio = pedir_radio()
resultado = calcular_volumen(radio)
mostrar_volumen(resultado)
