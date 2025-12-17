def solicitar_monto():
    monto = float(input("digite la cantidad de dinero de su cuenta: "))
    return monto

def aplicar_interes(monto):
    tasa = 0.05
    ganancia = monto * tasa
    suma_total = monto + ganancia
    return suma_total

def mostrar_mensaje(suma_total):
    print("el total a pagar (con 5 porciento de interés) es:", suma_total, "$")
    
# ************* codigo principal **************

cantidad = solicitar_monto()
resultado = aplicar_interes(cantidad)
mostrar_mensaje(resultado)
