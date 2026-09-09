class unHumano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def metodo(self):
        return 'Método normal', self

    @classmethod
    def metododeclase(cls):
        return 'Método de clase'

    @staticmethod
    def metodoestatico():
        return "Método estático"
    
    
humano1 = unHumano("juan",20)
print(humano1.nombre)
print(unHumano.metododeclase())