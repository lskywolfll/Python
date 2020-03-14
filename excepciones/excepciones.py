

def divide_elementos_de_lista(lista, divisor):
    # Defender la funcionalidad!
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        return lista
    # Se ejecuta al final por el cual puedes hacer otra cosa fuera de esta logica que tiene la funcion en si o simplemente hacer alguna otra cosa dentro de la funcion al finalizar todo
    finally:
        print('Se ejecuto correctamente sin problemas')

lista = list(range(10))
divisor = 1

print(divide_elementos_de_lista(lista, divisor))