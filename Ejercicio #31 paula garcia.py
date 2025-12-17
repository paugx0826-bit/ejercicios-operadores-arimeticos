def solicitar_horas():
    horas = float(input("ingrese la cantidad de horas para pasar a minutos: "))
    return horas

def convertir_minutos(horas):
    minutos = horas * 60
    return minutos

def imprimir_mensaje(minutos, horas):
    print(horas, " son: ", minutos, " minutos")
    
# ********** codigo principal **********

horas = solicitar_horas()
minutos = convertir_minutos(horas)
imprimir_mensaje(minutos, horas)
