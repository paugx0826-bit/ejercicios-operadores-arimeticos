def calcular_volumen_prisma(largo, base, alto):
    resultado_volumen = largo * base * alto
    return resultado_volumen

medida_largo = float(input("Digite la medida del largo del prisma: "))
medida_base = float(input("Digite la medida del ancho del prisma: "))
medida_alto = float(input("Digite la medida de la altura del prisma: "))

volumen_final = calcular_volumen_prisma(medida_largo, medida_base, medida_alto)
print(f"El resultado del volumen del prisma es: {volumen_final}")
