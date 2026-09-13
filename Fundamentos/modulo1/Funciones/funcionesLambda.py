suma = lambda a, b: a + b
print(suma(2, 4))

#usarla como arguento
def mi_funcion(lambda_func):
    return lambda_func(2,4)
mi_funcion(lambda a, b: a + b)

#tambien podemos especificar el parametro
(lambda a, b, c: a + b + c)(a=1, b=2, c=3) # 6

#con args y kwargs
(lambda *args: sum(args))(1, 2, 3) # 6
(lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3) # 6

#Decoradores

def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)

# Se va a llamar
# Entra en funcion suma
# Se ha llamado


def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)
# Imprimer esto antes y después
# Entra en funcion suma
# Imprimer esto antes y después