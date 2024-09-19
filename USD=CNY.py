def convertir_usd_a_cny(usd):
    tasa_conversion = 6.75  # Ejemplo de tasa de conversión (actualízala según la tasa actual)
    cny = usd * tasa_conversion
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
usd = 15
resultado = convertir_usd_a_cny(usd)
print(resultado)
