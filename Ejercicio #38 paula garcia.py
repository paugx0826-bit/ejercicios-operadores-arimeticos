def capturar_numeros():
    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))
    return x, y

def obtener_mayor(x, y):
    if x > y:
        return x
    else:
        return y

def mostrar_mayor(mayor):
    print("El número mayor es:", mayor)

# PROGRAMA PRINCIPAL
n1, n2 = capturar_numeros()
mayor = obtener_mayor(n1, n2)
mostrar_mayor(mayor)
