objetivo = int(input('Escoge un numero: '))
# Precision
epsilon = 0.001
# limite inferior
bajo = 0.0
# limite superior
alto = max(1.0, objetivo)

respuesta = (alto + bajo) / 2

# Derecha => alto
# izquierda => bajo

# MIsion disminuir a la mitad la busqueda

while abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta ** 2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    # Divivir entre 2 el espacio de busqueda por ende solo la mitad
    respuesta  = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')