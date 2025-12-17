def solicitar_dividendo():
    valor1 = int(input("ingrese el número dividendo: "))
    return valor1

def solicitar_divisor():
    valor2 = int(input("ingrese el número divisor: "))
    return valor2

def calcular_cociente(valor1, valor2):
    resultado = valor1 / valor2
    return resultado

def imprimir_resultado(resultado):
    print("el cociente de la división es:", resultado)
    
# *********** codigo principal *****************

dividendo = solicitar_dividendo()
divisor = solicitar_divisor()
cociente = calcular_cociente(dividendo, divisor)
imprimir_resultado(cociente)
