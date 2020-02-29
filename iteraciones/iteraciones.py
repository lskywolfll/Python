
# contador = 0

# while contador < 10:
#     contador += 1
#     print(contador)


# contador_externo = 0
# contador_interno = 0

# while contador_externo < 5:
#     while contador_interno < 6:
#         print(contador_externo, contador_interno)
#         contador_interno += 1
#     contador_externo += 1
#     contador_interno = 0

# Iteracion con objetos

frutas = ['Naranja', 'Pera', 'Manzana', 'Frutilla', 'Piña', 'Limon', 'Cereza', 'Melon', 'Chirimolla', 'Durazno']
frutasVacias = []
# For nombre in objeto:
#   /*code*/
for fruta in frutasVacias:
    print(fruta)
else:
    print('Tengo vida cuando termina el recorrido completo o cuando no tiene nada')

# Iteracion cuando desconocemos el tipo de recorrido por el cual va
# creamos un iterador para ese tipo de datos con iter(dato)
# Cada vez que queramos ver el siguiente dato usaremos el next(iterador) el cual nos dara el valor siguiente

iterador = iter(frutas)
cantidadDeDatos = len(frutas)

# for i in range(0, cantidadDeDatos):
#     print(next(iterador))
countIter = sum(1 for _ in iter(frutas))

for i in range(0, countIter):
    print(next(iterador))