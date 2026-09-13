class unHumano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def metodo(self):
        return 'Método normal'

    @classmethod
    def metododeclase(cls):
        return 'Método de clase'

    @staticmethod
    def metodoestatico():
        return "Método estático"
    
    
humano1 = unHumano("juan",20)
print(humano1.nombre)
print(unHumano.metododeclase())


# ------------------------------------------
#modificador de acceso private
# ------------------------------------------

class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!
print(dir(mi_clase))