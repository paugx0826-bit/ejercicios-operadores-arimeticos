def calcular_area_cuadrado(lado):
    resultado_area = lado ** 2
    return resultado_area

medida_lado = float(input("Digite la medida del lado: "))
area_final = calcular_area_cuadrado(medida_lado)

print(f"El resultado del área del cuadrado es: {area_final}")
