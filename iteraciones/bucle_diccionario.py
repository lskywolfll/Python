estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

# Obtenemos solos nombres de la palabra clave
for pais in estudiantes:
    print(pais)
# Obtenemos lo mismo que el anterior
for keys in estudiantes.keys():
    print(keys)
# Obtenemos los valores de la palabra clave creada
for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)
# (╯°□°）╯︵ ┻━┻) obtenemos la palabra clave con su valor
for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)

# "break" termina el bucle y permite continuar con el resto del flujo de nuestro programa.

# "continue" termina la iteración en curso y continua con el siguiente ciclo de iteración.
# break EJ :
for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)
    if pais == 'mexico':
        break

for keys in estudiantes.keys():
    print('Continue: ', keys)
    for numero_de_estudiantes in estudiantes.values():
        if numero_de_estudiantes == 10:
            print(numero_de_estudiantes)
            continue
