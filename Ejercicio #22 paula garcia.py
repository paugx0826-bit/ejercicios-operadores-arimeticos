def solicitar_numeros():
    valor_x = float(input("Ingrese el primer valor: "))
    valor_y = float(input("Ingrese el segundo valor: "))
    return valor_x, valor_y

def calcular_diferencia(valor_x, valor_y):
    resultado = valor_x - valor_y
    return resultado

def imprimir_diferencia(resultado):
    print("El resultado de la resta es:", resultado)

x, y = solicitar_numeros()
diferencia = calcular_diferencia(x, y)
imprimir_diferencia(diferencia)
