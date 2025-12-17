def solicitar_kilometros():
    km = float(input("digite la cantidad de kilómetros para convertir a millas: "))
    return km

def realizar_conversion(km):
    factor = 0.621
    resultado = km * factor
    return resultado

def mostrar_conversion(resultado):
    print("los kilómetros digitados a millas son:", resultado)
    
# *************** codigo principal ****************

kilometros = solicitar_kilometros()
millas = realizar_conversion(kilometros)
mostrar_conversion(millas)
