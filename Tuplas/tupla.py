# Tuplas
# Son datos que jamas se pueden cambiar
# Pueden contener cualquier tipo de dato que quieras
# Pueden utilizarse para devolver valores obtenidos mediante una funcion
# Se puede reasignar la tupla creada para la variable para insertar otros valores pero no podemos de por si modficar los datos que tengan en una posicion dada de la tupla

# Ejemplo de tutpla
tupla_inicial = ()

tupla_reasignable = ()
# Lo curioso que nosotros podemos recorrer la tupla como una cajita(array) por el cual obtener los datos desde la posicion inicial de este a partir desde el 0 a n elementos que tengamos dentro de la tupla
tupla_reasignable = ('hola', 'como estas', 'adios')

print(tupla_reasignable[2])

primerNumeroTupla = (1,)
sumaDeTupla = (2,3,4)

primerNumeroTupla += sumaDeTupla

print(primerNumeroTupla)

# Desestructurar objetos
# variables por las posicion de los objetos recordar que es una cajita(array)
# ej: 
# cajita = (1,2,3,4,5)
# destructuracion
# primerNumero,segundoNumero,tercerNumero,cuartoNumero = cajita
# print(primerNumero) = 1 Ta Da!!

# Tener en mente que estas variables van desde la ultima posicion en adelante 
x, y, z = sumaDeTupla

print(x)
print(y)
print(z)