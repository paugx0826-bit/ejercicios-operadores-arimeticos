def solicitar_precio():
    valor = float(input("digite el precio del artículo: "))
    return valor

def aplicar_descuento(valor):
    porcentaje = 0.10
    rebaja = valor * porcentaje
    monto_final = valor - rebaja
    return monto_final

def mostrar_total(monto_final):
    print("el precio total a pagar es:", monto_final)

# ******** código principal ************

precio_articulo = solicitar_precio()
precio_con_descuento = aplicar_descuento(precio_articulo)
mostrar_total(precio_con_descuento)
