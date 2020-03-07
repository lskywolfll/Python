def multiplicar_por_dos(n):
    return n * 2


def sumar_dos(n):
    return n + 2


def aplicar_operacion(f, numeros):
    # F es una funcione por ende podemos usarla como un callback(llamada de vuelta) conjunto a sus parametros que pide o en caso contrario simplemente haga el trabajo que tiene que hacer
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    # Se retornan los datos para ser asignadas a una variable
    return resultados


nums = [1, 2, 3]

multiplicarPorDos = aplicar_operacion(multiplicar_por_dos, nums)
sumarDos = aplicar_operacion(sumar_dos, nums)

print(multiplicarPorDos)
print(sumarDos)

# Funciones anonimas
# lambda <Parametros>:<lo que quieres hacer usando los parametros>


def elevados(numero, elevado): return numero ** elevado


print(elevados(10, 2))

# operaciones listadas por cada dato
def aplicar_operaciones(num):
    # funciones para ser utilizadas como callback
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-10))

