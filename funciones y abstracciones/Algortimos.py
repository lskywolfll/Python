from datetime import datetime

def aproximacion():
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

    print(f'Comenzo a las {tiempoInicio} y termino a las {tiempoFinal}')
    Lista()

def enumeracionExhaustiva():
    objetivo = int(input('¿Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
    
    Lista()

def busquedaBinaria():
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
    Lista()

def eleccion(opcion):
    if opcion == 1:
        aproximacion()
    elif opcion == 2:
        enumeracionExhaustiva()
    elif opcion == 3:
        busquedaBinaria()
    elif opcion == 4:
        print('Muchas gracias por usar nuestros sistemas!!')
    else:
        print('Solo puedes seleccionar los algoritmos de la lista, te devolveremos al inicio')
        Lista()

def Lista():
    print(""" 
            Cual algoritmo deseas usar para obtener la raiz cuadrada ?

            ====================Lista==================
            1- Aproximacion
            2- Enumeracion Exhaustiva
            3- Busqueda Binaria
            4- Salir
    """)
    opcion = int(input('Yo escogere: '))
    eleccion(opcion)

if __name__ == '__main__':
    Lista()