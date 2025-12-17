def pedir_valores():
    valor_a = float(input("Ingrese el primer número: "))
    valor_b = float(input("Ingrese el segundo número: "))
    return valor_a, valor_b

def calcular_division(valor_a, valor_b):
    resultado = valor_a / valor_b
    return resultado

def mostrar_resultado(resultado):
    print("El resultado de la división es:", resultado)

a, b = pedir_valores()
cociente = calcular_division(a, b)
mostrar_resultado(cociente)
