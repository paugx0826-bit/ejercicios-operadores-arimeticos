def ingresar_valores():
    dato_uno = float(input("Ingrese el primer número: "))
    dato_dos = float(input("Ingrese el segundo número: "))
    return dato_uno, dato_dos

def calcular_producto(dato_uno, dato_dos):
    resultado = dato_uno * dato_dos
    return resultado

def mostrar_resultado(resultado):
    print("El resultado de la multiplicación es:", resultado)

a, b = ingresar_valores()
total = calcular_producto(a, b)
mostrar_resultado(total)
