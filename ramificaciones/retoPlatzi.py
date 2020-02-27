# Que se ingrese un nombre y edad para luego compararlos para indicar cual de las dos personas(como minimo) es mayor

class Persona(object):
    def __init__(self, Nombre, Edad):
        self.nombre = Nombre
        self.edad = Edad
    # Cuando ponemos parametros para las funciones dentro de un objeto siempre debemos usar el self para que estemos referenciando siempre al mismo objeto
    def compararEdades(self,persona):
        if self.edad > persona.edad:
            print(f'{self.nombre} es mayor que {persona.nombre} por {self.edad - persona.edad} años')
        elif self.edad < persona.edad:
            print(f'{self.nombre} es menor que {persona.nombre} por {persona.edad - self.edad} años')
        else:
            print(f'{self.nombre} tiene la misma edad que {persona.nombre}!!! 🤯')
        

primeraPersona = Persona(input('Cual es tu nombre ?\n'), int(input('Cual es tu edad ?\n')))

segundaPersona = Persona(input('Cual es tu nombre ?\n'), int(input('Cual es tu edad ?\n')))

primeraPersona.compararEdades(segundaPersona)