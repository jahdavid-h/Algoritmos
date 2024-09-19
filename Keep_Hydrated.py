'''
Mantente hidratado
'''

import math

def agua_bebida(tiempo):
    litros = tiempo * 0.5
    return math.floor(litros)

# Ejemplo de uso
tiempo = 11.8
resultado = agua_bebida(tiempo)
print(f"Nathan beberá {resultado} litros de agua.")
