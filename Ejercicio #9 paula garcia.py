def solicitar_dimensiones():
    """Solicita al usuario las bases y la altura del trapecio."""
    base_mayor = float(input("Ingrese la longitud de la base mayor (B): "))
    base_menor = float(input("Ingrese la longitud de la base menor (b): "))
    altura = float(input("Ingrese la altura del trapecio (h): "))
    return base_mayor, base_menor, altura

def obtener_magnitud(base_mayor, base_menor, altura):
    """Calcula el área del trapecio con la fórmula: A = (B + b) * h / 2."""
    area = ((base_mayor + base_menor) * altura) / 2
    return area

def desplegar_informacion(area):
    """Muestra el área calculada."""
    print(f"El área del trapecio es: {area:.2f} unidades cuadradas")

# Código principal
if __name__ == "_main_":
    B, b, h = solicitar_dimensiones()
    magnitud = obtener_magnitud(B, b, h)
    desplegar_informacion(magnitud)