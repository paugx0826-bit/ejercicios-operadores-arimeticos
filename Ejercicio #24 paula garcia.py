def solicitar_numero():
    valor = float(input("Ingrese un número: "))
    return valor

def elevar_al_cuadrado(valor):
    resultado = valor * valor
    return resultado

def imprimir_resultado(resultado):
    print("El resultado del número al cuadrado es:", resultado)

dato = solicitar_numero()
potencia = elevar_al_cuadrado(dato)
imprimir_resultado(potencia)
