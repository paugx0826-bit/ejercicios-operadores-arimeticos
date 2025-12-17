def pedir_celsius():
    c = float(input("Ingrese grados Celsius: "))
    return c

def convertir_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

def mostrar_temp(f):
    print("Temperatura en Fahrenheit:", f)

# PROGRAMA PRINCIPAL
celsius = pedir_celsius()
fahrenheit = convertir_fahrenheit(celsius)
mostrar_temp(fahrenheit)
