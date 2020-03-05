
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

print(my_lista)

my_lista.remove('Adios')

print(my_lista)

my_lista.pop(1)

print(my_lista)

for cosa in my_lista:
    print(cosa)

# Proteccion de datos de las listas

# Cambio de valor en la variable cuando se toma el valor de un punto de la lista por el cual cambia cuando se vuelve a cambiar datos en la lista

listaVulnerable = [1,2,3]
copiaListaVulnerable = listaVulnerable
# Perdida de valor al hacer un cambio

# copiaDeValores = [listaVulnerable, copiaListaVulnerable]
# listaVulnerable.append(4)

# Persistencia de valor
copiaInmutable = list(copiaListaVulnerable)
print(copiaInmutable)
listaVulnerable.append(4)
# lista[posicionInicial:posicionFinal] por el cual hace una ordenanza desde el 1 elemento en adelante
# lista[::posicionFinal] por el cual este se ordena desde el ultimo elemento en adelante
print(copiaInmutable[::-1])

# Otra forma de ordenamiento inverso o normal
copiaInmutable.sort()
print(copiaInmutable)
# Este tambien cambia el valor contenido en la lista para que ahora sea inverso
copiaInmutable.sort(reverse=True)
print(copiaInmutable)

# Invertir la lista (Modificarla)
copiaInmutable.reverse()
print(copiaInmutable)

print(id(listaVulnerable))
print(id(copiaInmutable))

# print(copiaDeValores)