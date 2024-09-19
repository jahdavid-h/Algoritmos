'''
Formato de decimales
'''

def redondear_a_dos_decimales(numero):
    return round(numero, 2)

# Prueba de la función
numero = 3.3424
resultado = redondear_a_dos_decimales(numero)
print(resultado)  # Resultado: 12.35
