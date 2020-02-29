
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

# Hipotesis
# Cuando ponemos un else en el ciclo definido del for esto nos indica que cuando termine o no encuentre nada por recorrer este se ejecutara ^_^

# Ejemplo cuando no tiene nada
for fruta in frutasVacias:
    print(fruta)
else:
    print('Tengo vida cuando termina el recorrido completo o cuando no tiene nada\n')
# Ejemplo cuando termina con el recorrido de los datos que pueda poseer
for fruta in frutas :
    print(fruta)
else:
    print('Tengo vida cuando termina el recorrido completo o cuando no tiene nada\n')

# Iteracion cuando desconocemos el tipo de recorrido por el cual va
# creamos un iterador para ese tipo de datos con iter(dato)
# Cada vez que queramos ver el siguiente dato usaremos el next(iterador) el cual nos dara el valor siguiente

# 1 Forma
iterador = iter(frutas)
cantidadDeDatos = len(frutas)

# for i in range(0, cantidadDeDatos):
#     print(next(iterador))

# 2 Forma
# Si intercambiamos el iter(frutas) por el iterador que creamos anteriormente luego no podremos ver los datos que contiene este ya que este lo transforma para obtener la cantidad de datos que contiene 🤯!!
# por esto debemos nosotros crear nuevamente el iterador a quien queremos crear para que de esa forma transforme ello y no afecte el dato por el cual nosotros vamos a imprimir los datos o usarlos
cantidadDeDatosDelIterador = sum(1 for _ in iter(frutas))

for i in range(0, cantidadDeDatosDelIterador):
    print(next(iterador))

# NT: Cuando recorremos un iterador no podemos volver a recorrerlo por ello solo puedas hacerlo con la forma que tu desees