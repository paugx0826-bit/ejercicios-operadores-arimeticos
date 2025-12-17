def pedir_datos():
    base = float(input("Ingrese la base: "))
    ancho = float(input("Ingrese el ancho: "))
    altura = float(input("Ingrese la altura: "))
    return base, ancho, altura

def calcular_volumen(base, ancho, altura):
    volumen = (base * ancho * altura) / 3
    return volumen

def mostrar_volumen(volumen):
    print("El volumen de la pirámide es:", volumen)

# PROGRAMA PRINCIPAL
b, a, h = pedir_datos()
vol = calcular_volumen(b, a, h)
mostrar_volumen(vol)
