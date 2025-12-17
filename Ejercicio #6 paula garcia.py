# Función 1: Verifica si el número es positivo
def validar_positivo(numero):
    """Retorna True si el número es mayor que cero."""
    return numero > 0

# Función 2: Verifica si el número es negativo
def validar_negativo(numero):
    """Retorna True si el número es menor que cero."""
    return numero < 0

# Función 3: Verifica si el número es neutro (cero)
def validar_neutro(numero):
    """Retorna True si el número es igual a cero."""
    return numero == 0

# Función principal para solicitar la entrada e imprimir el resultado
def identificar_signo():
    """
    Solicita un número al usuario y determina si es positivo,
    negativo o neutro usando las tres funciones definidas.
    """
    try:
        # Solicitar al usuario que ingrese un número
        entrada = input("Por favor, introduce un número: ")
        numero = float(entrada) # Convertir la entrada a un número decimal

        # Usar las funciones para identificar el tipo de número
        if validar_positivo(numero):
            print(f"El número {numero} es **POSITIVO** **⬆️**.")
        elif validar_negativo(numero):
            print(f"El número {numero} es **NEGATIVO** **⬇️**.")
        elif validar_neutro(numero):
            print(f"El número {numero} es **NEUTRO** (Cero) **0️⃣**.")
        
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número real.")

# Ejecutar la función principal
if __name__ == "__main__":
    identificar_signo()