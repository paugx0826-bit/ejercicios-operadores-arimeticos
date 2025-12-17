def solicitar_cantidad():
    cantidad_litros = float(input("Digite la cantidad de litros: "))
    return cantidad_litros

def convertir_a_galones(cantidad_litros):
    total_galones = cantidad_litros * 2.54
    return total_galones

def presentar_conversion(total_galones):
    print("La equivalencia en galones es:", total_galones)

valor_litros = solicitar_cantidad()
valor_galones = convertir_a_galones(valor_litros)
presentar_conversion(valor_galones)
