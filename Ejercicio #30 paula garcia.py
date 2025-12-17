def solicitar_radio():
    valor_radio = float(input("Ingrese el radio del círculo: "))
    return valor_radio

def obtener_circunferencia(valor_radio):
    pi = 3.1415
    resultado = (valor_radio * 2) * pi
    return resultado

def imprimir_resultado(resultado):
    print("La longitud de la circunferencia es:", resultado)

# código principal
radio_circulo = solicitar_radio()
circunferencia = obtener_circunferencia(radio_circulo)
imprimir_resultado(circunferencia)
