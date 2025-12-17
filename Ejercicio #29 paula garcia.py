def solicitar_numero():
    valor = int(input("Ingrese un número entero: "))
    return valor

def comprobar_paridad(valor):
    if valor % 2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

# programa principal
dato = solicitar_numero()
comprobar_paridad(dato)
