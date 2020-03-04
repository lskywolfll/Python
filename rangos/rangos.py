# Rangos
# Son una secuencia de valores enteros
# Tambien al igual que al utilizar las tuplas son datos inmutables
# Son bastantes benos en el consumo de memoria y normalmente para ciclos definidos con un fin

# range(comienzo, fin, pasos)
# Al llegar al fin no tomara el valor en si osea ej: range(1,5) => 1,2,3,4 menos el 5!

my_range = range(1, 5)

for i in my_range:
    print(i)

rangoInicial = range(0, 7, 2)
rangoFinal = range(0, 8, 2)

# Igualdad simple
print(f'igualdad simple: {rangoInicial == rangoFinal}')
# Igualdad estricta
print(f'igualdad estricta: {rangoInicial is rangoFinal}')
# espacio en memoria
print(id(rangoInicial))
print(id(rangoFinal))