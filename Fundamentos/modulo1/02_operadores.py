# Variables iniciales
total_factura = 150
cantidad_personas = 4

# Operaciones básicas
suma = total_factura + 20           # 170
impuesto = total_factura * 0.19     # 28.5 (19% de IVA)

# Diferencia entre divisiones
pago_exacto = total_factura / cantidad_personas   # 37.5 (Float)
pago_entero = total_factura // cantidad_personas  # 37 (Entero)

# Módulo (saber si un número es par o impar)
es_par = cantidad_personas % 2      # 0 (porque 4 es divisible por 2)

# Exponenciación
area_cuadrado = 5 ** 2              # 25

edad = 20
tiene_licencia = True
infracciones = 0



# Asignación básica
puntos_vida = 100
nivel = 1

# Recibir daño (Resta y asigna)
puntos_vida -= 25  
# puntos_vida ahora es 75

# Subir de nivel (Suma y asigna)
nivel += 1         
# nivel ahora es 2

# Aplicar un multiplicador de bonificación (Multiplica y asigna)
monedas = 50
monedas *= 1.5     
# monedas ahora es 75.0

# Asignación múltiple en una sola línea (Característica muy útil en Python)
x, y, z = 10, 20, 30



# Uso de 'and': Ambas condiciones deben cumplirse
if edad >= 18 and tiene_licencia:
    print("Permiso para alquilar vehículo concedido.")
else:
    print("No cumples con los requisitos básicos.")

# Uso de 'or': Al menos una condición debe cumplirse
# Uso de 'not': Invierte el resultado de la condición
if (infracciones > 3) or not tiene_licencia:
    print("Alerta: Conductor de alto riesgo o sin licencia.")
elif edad < 21 and infracciones == 0:
    print("Conductor joven, pero con buen historial. Tarifa estándar.")
else:
    print("Conductor apto.")

    temperatura = 22

# Estilo Python (Encadenado)
if 15 < temperatura < 25:
    print("Clima agradable")