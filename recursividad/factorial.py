def factorial(n):
    """ Calcula el factorial de n

    va desde n hasta el 1
    ej: 4 * 3 * 2 * 1 = 24

    primer recorrido
    4 *
    segundo
    4 * 3
    tercero
    4 * 3 * 2
    cuarto 
    4 * 3 * 2 * 1 = 24

    Al llamarse asi misma cuando saca el factorial se acumula hasta que le indiquemos cuando pare que en este punto es 1

    n int > 0
    return n!(numeros factoriables por el cual llega el numero ej: 1 * 2 * 3 * 4)
    """
    print('Valor: ', n)
    print(f'valor multiplicado {n} * {n - 1}: ', n * (n - 1))
    if n == 1:
        return 1
   
    return n * factorial(n - 1)

numero = int(input('Escribe un entero: '))

print(factorial(numero))