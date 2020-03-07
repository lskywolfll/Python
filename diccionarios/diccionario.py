# palabra clave : valor
mi_diccionario = {
    "Rene":20,
    "Erika":32,
    "Jaime":50,
}
# Recorrer los valores que posee el diccionario
for persona,edad in mi_diccionario.items():
    print(persona, edad)

# Eliminar diccionario
del mi_diccionario['Erika']

# Verificar si existe una palabra clave en la lista
print("René" in mi_diccionario)