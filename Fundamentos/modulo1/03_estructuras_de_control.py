#condicional simple
calificacion = 85

# Los dos puntos (:) indican que comienza un bloque
if calificacion >= 90:
    # La identación (4 espacios) indica que esto está dentro del 'if'
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")

#Condicional en variable
    edad = 20

# En Java/Dart sería: estado = (edad >= 18) ? "Mayor" : "Menor";
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"

print(estado) # Imprime: Mayor de edad

#Switch case

codigo_error = 404

match codigo_error:
    case 200:
        print("Éxito (OK)")
    case 404:
        print("No encontrado (Not Found)")
    case 500:
        print("Error interno del servidor")
    # El guion bajo (_) funciona como el 'default'
    case _:
        print("Código de error desconocido")
        
 # Una tupla que representa coordenadas (x, y)
punto = (0, 15)
#se le puede añadir condicionales
match punto:
    case (0, 0):
        print("Estás exactamente en el origen.")
    case (0, y):
        # Coincide si x es 0. Además, guarda el valor de y en la variable 'y'.
        print(f"Estás en el eje Y, a una altura de {y}.")
    case (x, 0):
        print(f"Estás en el eje X, en la posición {x}.")
    case (x, y):
        print(f"Estás en un punto cualquiera: {x}, {y}.")

#Bucles for & while

#While

contador = 0

while contador < 3:
    print(f"Número: {contador}")
    # Recuerda: Python no tiene contador++, debes usar += 1
    contador += 1
    
    
#For

# Imprime del 0 al 4 (el 5 no se incluye)
for i in range(5):
    print(i)

# Imprime del 2 al 6 (empieza en 2, termina antes de 7)
for i in range(2, 7):
    print(i)

# Imprime números pares del 0 al 10 (con saltos de 2)
for i in range(0, 11, 2):
    print(f"Par: {i}")

# Cuenta regresiva (saltos negativos)
for i in range(5, 0, -1):
    print(i)
    
    
#ForEach

lenguajes = ["Java", "Dart", "Python"]

# "Por cada lenguaje en la lista lenguajes..."
for lenguaje in lenguajes:
    print(f"Me gusta programar en {lenguaje}")
    
# También puedes iterar sobre una cadena de texto letra por letra
for letra in "Hola":
    print(letra)

#For con Continue y Break

for i in range(1, 10):
    if i == 3:
        continue # Salta el número 3
    if i == 6:
        break    # Detiene el bucle al llegar al 6
    print(i)
# Resultado: Imprimirá 1, 2, 4, 5