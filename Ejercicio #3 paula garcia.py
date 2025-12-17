#Funciones
base=10
altura= 5

def encontrar_datos(base, altura):
    area=(base * altura)/2
    return area

def dar_total(area):
    print (f"El resultado es: {area}")

def mensaje(area):
    print("Este es el area del rectangulo ")

#Zona de codigo principal

print("CALCULA EL AREA DEL RECTANGULO\n")

area_rect=encontrar_datos(base, altura)
dar_total(area_rect)
mensaje(area_rect)