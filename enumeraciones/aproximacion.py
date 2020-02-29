from datetime import datetime

objetivo = int(input('Escoge un numero: '))

epsilon = 0.01
paso = epsilon ** 2
respuesta = 0.0
tiempoInicio = datetime.now()
while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    tiempoFinal = datetime.now()

print(f'Comenzo a las {tiempoInicio}\n y termino a las {tiempoFinal}')