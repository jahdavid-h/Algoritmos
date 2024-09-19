def rango_citas(edad):
    if edad <= 14:
        # Fórmula especial para edades <= 14
        min_age = int(edad - 0.10 * edad)
        max_age = int(edad + 0.10 * edad)
    else:
        # Regla clásica: la mitad de la edad más 7
        min_age = int(edad / 2 + 7)
        max_age = int((edad - 7) * 2)

    return f"{min_age}-{max_age}"


# Ejemplo de uso
edad = 19
resultado = rango_citas(edad)
print(f"El rango de edad recomendado para alguien de {edad} años es: {resultado}")
