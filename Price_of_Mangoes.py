'''
Promocion de mangos 3x2
'''

def costo_total_mangos(cantidad, precio_por_mango):
    # Calcular cuántos mangos se pagan según la oferta
    pagados = (cantidad // 3) * 2 + (cantidad % 3)
    # Calcular el costo total
    costo_total = pagados * precio_por_mango
    return costo_total

# Ejemplo de uso
cantidad_mangos = 9
precio_por_mango = 5
resultado = costo_total_mangos(cantidad_mangos, precio_por_mango)
print(f"El costo total es: ${resultado}")
