class Comuna(object):
    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def datosVisibles(self):
        print(self.nombre)
        print(self.apellido)

Comuna('Arica', 10312312).datosVisibles()