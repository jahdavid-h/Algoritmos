def calcular_presion_total(M1, M2, m1, m2, V, T_Celsius):
    # Constante de los gases (en las unidades apropiadas)
    R = 0.082  # dm^3 * atm * K^-1 * mol^-1

    # Convertir la temperatura de Celsius a Kelvin
    T_Kelvin = T_Celsius + 273.15

    # Calcular la presión total usando la fórmula
    P_total = ((m1 / M1) + (m2 / M2)) * (R * T_Kelvin) / V

    return P_total


# Ejemplo de uso
M1 = 18  # Masa molar del primer gas (g/mol)
M2 = 32  # Masa molar del segundo gas (g/mol)
m1 = 10  # Masa actual del primer gas (g)
m2 = 5  # Masa actual del segundo gas (g)
V = 10  # Volumen del recipiente (dm^3)
T_Celsius = 25  # Temperatura en grados Celsius

presion_total = calcular_presion_total(M1, M2, m1, m2, V, T_Celsius)
print(f"La presión total es: {presion_total:.2f} atm")
