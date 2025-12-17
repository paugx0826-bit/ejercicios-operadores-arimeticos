def solicitar_medidas():
    valor_base = float(input("Ingrese el valor de la base: "))
    valor_altura = float(input("Ingrese el valor de la altura: "))
    return valor_base, valor_altura

def calcular_area_triangulo(valor_base, valor_altura):
    resultado_area = valor_base * valor_altura
    return resultado_area

def mostrar_resultado(resultado_area):
    print("El resultado del área del triángulo es:", resultado_area)

b, h = solicitar_medidas()
area_final = calcular_area_triangulo(b, h)
mostrar_resultado(area_final)
