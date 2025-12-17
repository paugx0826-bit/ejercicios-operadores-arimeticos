def leer_medida():
    valor_pulgadas = float(input("Digite la cantidad en pulgadas: "))
    return valor_pulgadas

def convertir_a_centimetros(valor_pulgadas):
    resultado_cm = valor_pulgadas * 2.54
    return resultado_cm

def imprimir_resultado(resultado_cm):
    print("La medida en centímetros es:", resultado_cm)

dato_pulgadas = leer_medida()
dato_cm = convertir_a_centimetros(dato_pulgadas)
imprimir_resultado(dato_cm)
