def obtener_medidas():
    valor_base = float(input("Digite el valor de la base: "))
    valor_altura = float(input("Digite el valor de la altura: "))
    return valor_base, valor_altura

def calcular_area(valor_base, valor_altura):
    resultado = valor_base * valor_altura
    return resultado

def presentar_resultado(resultado):
    print(f"El resultado del área del paralelogramo es: {resultado}")
    print("\n" + "-" * 50)
    print("-" * 50)

b, h = obtener_medidas()
area_paralelogramo = calcular_area(b, h)
presentar_resultado(area_paralelogramo)
