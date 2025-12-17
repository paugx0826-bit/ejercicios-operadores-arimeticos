def solicitar_numero():
    n = float(input("Ingrese un número: "))
    return n

def calcular_raiz(n):
    raiz = n ** 0.5
    return raiz

def mostrar_raiz(raiz):
    print("La raíz cuadrada es:", raiz)

# PROGRAMA PRINCIPAL
numero = solicitar_numero()
resultado = calcular_raiz(numero)
mostrar_raiz(resultado)
