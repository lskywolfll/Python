
# append (Agregar)
# pop (Borrar Ultimo elemento o posicion especifica)
# remove (Borrar elemento especifico) ej: lista.remove('Hola')  y lista tiene lista = ['Hola', 'Adios']
# insert (posicion, valor) => ingresamos un valor en una posicion conjunto a su valor pero cuando se inserta en esa posicion no borra si existe algun dato en la misma posicion
# Tener en mente cuando se inserta un valor en una posicion especifica si no existe nada despues de esa posicion o antes se ordenara al final de la lista
# ej: 
# listaDeFrutas = ['manzana','pera'] (Recordar que la posicion va desde el 0 a n)
# listaDeFrutas.insert(3, 'Naranja') (No existe la posicion 3) listaDeFrutas = ['manzana','pera', 'Naranja']
my_lista = []

my_lista.append('Hola')

my_lista.insert(1, 'Adios')

my_lista.insert(2, 'Hi!')

my_lista.insert(3, 'Chao')

print(f'Lista inicial: {my_lista}')

my_lista.remove('Adios')

print(f'Lista inicial borrando Adios: {my_lista}')

my_lista.pop(1)

print(f'Lista inicial borrando la posicion 1: {my_lista}')

for cosa in my_lista:
    print(f'valor dentro de la lista: {cosa}')

# Proteccion de datos de las listas

# Cambio de valor en la variable cuando se toma el valor de un punto de la lista por el cual cambia cuando se vuelve a cambiar datos en la lista

listaVulnerable = [1,2,3]
copiaListaVulnerable = listaVulnerable
# Perdida de valor al hacer un cambio

# copiaDeValores = [listaVulnerable, copiaListaVulnerable]
# listaVulnerable.append(4)

# Persistencia de valor
copiaInmutable = list(copiaListaVulnerable)
print(f'persistencia del valor usando una copia inmutable: {copiaInmutable}')
listaVulnerable.append(4)
# lista[posicionInicial:posicionFinal] por el cual hace una ordenanza desde el 1 elemento en adelante
# lista[::posicionFinal] por el cual este se ordena desde el ultimo elemento en adelante
print(f'ordenamiento inverso usando :: es: {copiaInmutable[::-1]}')

# Otra forma de ordenamiento inverso o normal
copiaInmutable.sort()
print(f'ordenamiento: {copiaInmutable}')
# Este tambien cambia el valor contenido en la lista para que ahora sea inverso
copiaInmutable.sort(reverse=True)
print(f'ordenamiento inverso: {copiaInmutable}')

# Invertir la lista (Modificarla)
copiaInmutable.reverse()
print(f'invertido: {copiaInmutable}')

print(f'identificador del objeto lista vulnerable: {id(listaVulnerable)}')
print(f'identificador del objeto copiaInmutable: {id(copiaInmutable)}')

# print(copiaDeValores)