def obtener_peso():
    peso_libras = float(input("Introduce el peso en libras: "))
    return peso_libras

def convertir_a_kilogramos(peso_libras):
    peso_kg = peso_libras * 0.45
    return peso_kg

def imprimir_resultado(peso_kg):
    print("El peso equivalente en kilogramos es:", peso_kg)

peso_en_libras = obtener_peso()
peso_en_kilogramos = convertir_a_kilogramos(peso_en_libras)
imprimir_resultado(peso_en_kilogramos)
