def leer_valores():
    valor_a = float(input("Ingrese el primer número: "))
    valor_b = float(input("Ingrese el segundo número: "))
    return valor_a, valor_b

def calcular_suma(valor_a, valor_b):
    resultado = valor_a + valor_b
    return resultado

def mostrar_resultado(resultado):
    print("El resultado de la suma es:", resultado)

a, b = leer_valores()
total = calcular_suma(a, b)
mostrar_resultado(total)
