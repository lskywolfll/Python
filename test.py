import datetime
import hug


# @hug.get(examples="name=Jhon Doe&amp;age=30")
# @hug.local()
# def say_hello(name: hug.types.text, age: hug.types.number, hug_timer=3):
#     """Decimos hola al usuario y calculamos su año de nacimiento"""
#     year_of_birth = datetime.datetime.now().year - age
#     return {
#         'message': "Hola {0}, naciste el año {1}".format(name, year_of_birth),
#         'took': float(hug_timer)
#     }


# if __name__ == '__main__':
#     print(say_hello("Gabriel", 23))

class Comuna(object):
    def __init__(self, nombre, cut, provincia, region):
        self.nombre = nombre
        self.cut = cut
        self.provincia = provincia
        self.region = region

def datosComunas(comuna):
    return {
        comuna.nombre,
        comuna.cut,
        comuna.provincia,
        comuna.region
    }

@hug.get()
@hug.local()
def comunasApi():
    comunas = [Comuna('Arica', 15101, 'Arica', 'Arica'), Comuna('Arica v2', 152020, 'Arica', 'Arica')]
    # for comuna in comunas:
    #     return {
    #         comuna.nombre,
    #         comuna.cut
    #     }
    # Cuando son muchos datos pasados por una lista entonces nosotros para poder devolver todos ellos debemos usar una funcion que recorra todo uno por uno
    return map(lambda comuna: { comuna.nombre, comuna.provincia, comuna.cut, comuna.region }, comunas)


if __name__ == '__main__':
    print(comunasApi())
