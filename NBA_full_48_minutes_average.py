def extrapolar_ppg(ppg, mpg):
    if mpg == 0:
        return 0
    # Extrapolamos los puntos por 48 minutos
    extrapolacion = (ppg / mpg) * 48
    # Redondeamos a la décima más cercana
    return round(extrapolacion, 1)

# Ejemplo de uso
ppg = 12
mpg = 20
resultado = extrapolar_ppg(ppg, mpg)
print(f"Puntos extrapolados por 48 minutos: {resultado}")
