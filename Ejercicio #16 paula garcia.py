def solicitar_medida():
    lado_cubo = float(input("Digite la longitud del lado del cubo: "))
    return lado_cubo

def calcular_volumen(lado_cubo):
    resultado_volumen = lado_cubo ** 3
    return resultado_volumen

def mostrar_resultado(resultado_volumen):
    print("El volumen calculado es:", resultado_volumen)

medida = solicitar_medida()
volumen_cubo = calcular_volumen(medida)
mostrar_resultado(volumen_cubo)

