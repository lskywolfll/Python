
def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        # Defendemos la funcionalidad !!
        assert type(palabra) == str, f'{palabra} no es texto'
        assert len(palabra) > 0, 'No se permiten textos vacios'
        primeras_letras.append(palabra[0])
    
    return primeras_letras
    

lista_de_palabras = ['1', '231', 1, '']

primera_letra(lista_de_palabras)