'''
Recorte de relacion de aspecto
'''


import math

def convert_to_16_9(x, y):
    #Relacion de aspecto 16:9
    aspect_ratio = 16 / 9
    #Calcular la nueva anchura (x) manteniendo la altura (Y)
    new_x = math.ceil(y * aspect_ratio)
    return new_x, y

#Ejemplos
test_resolutions = [(1920, 1080), (1440, 1080), (1024, 768), (800, 600)]
converted_resolutions = [convert_to_16_9(x, y) for x, y in test_resolutions]
print(converted_resolutions)