def solicitar_longitud():
    largo = float(input("digite la longitud del rectángulo: "))
    return largo

def solicitar_ancho():
    medida_ancho = float(input("digite el ancho del rectángulo: "))
    return medida_ancho

def calcular_area(largo, medida_ancho):
    resultado = largo * medida_ancho
    return resultado

def mostrar_area(resultado):
    print("el área del rectángulo es:", resultado)

# ************** código principal ***************

valor_longitud = solicitar_longitud()
valor_ancho = solicitar_ancho()
area_rectangulo = calcular_area(valor_longitud, valor_ancho)
mostrar_area(area_rectangulo)
