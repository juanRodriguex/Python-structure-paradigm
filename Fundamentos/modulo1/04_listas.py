# ==========================================
# CLASE 4: LISTAS Y TUPLAS
# ==========================================

# ------------------------------------------
# 1. LISTAS (list)
# ------------------------------------------
my_list = list()
my_other_list = []

print(len(my_list))  # 0

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))  # 7

my_other_list = [35, 1.77, "Brais", "Moure", "Dev"]

print(type(my_list))        # <class 'list'>
print(type(my_other_list))  # <class 'list'>

# Acceso a elementos e índices
print(my_other_list[0])   # 35 (primer elemento)
print(my_other_list[1])   # 1.77
print(my_other_list[-1])  # "Dev" (último elemento)
print(my_other_list[-3])  # "Brais"
print(my_list.count(30))  # 2 (cuenta cuántas veces aparece el 30)

# Desempaquetado (Unpacking)
age, height, name, surname, alias = my_other_list
print(name)  # Brais

# Concatenación de listas
print(my_list + my_other_list)

# Modificación de elementos
my_other_list[0] = 36
my_other_list[2] = "Brais Moure"
print(my_other_list)

# --- Métodos de Listas ---

# append: Agrega un elemento al final
my_other_list.append("MoureDev")
print(my_other_list)

# insert: Inserta un elemento en una posición específica (índice, valor)
my_other_list.insert(1, "Rojo")
print(my_other_list)

# remove: Elimina la primera aparición de un elemento por su valor
my_other_list.remove("Rojo")
print(my_other_list)

my_list.remove(30)  # Elimina el primer 30
print(my_list)

# pop: Elimina y retorna el último elemento (o el del índice indicado)
my_pop_element = my_list.pop()
print(my_pop_element)  # 17
print(my_list)

pop_index_element = my_list.pop(2)
print(pop_index_element)  # 52
print(my_list)

# del: Elimina un elemento por su índice (o borra la variable completa)
del my_list[2]
print(my_list)

# copy: Crea una copia independiente de la lista
my_new_list = my_list.copy()

# clear: Vacía todos los elementos de la lista
my_list.clear()
print(my_list)      # []
print(my_new_list)  # Conserva los elementos copiados

# reverse: Invierte el orden de los elementos de la lista
my_new_list.reverse()
print(my_new_list)

# sort: Ordena los elementos (de menor a mayor o alfabéticamente)
my_new_list.sort()
print(my_new_list)

# Sort descendente
my_new_list.sort(reverse=True)
print(my_new_list)

# Sublistas (Slicing)
print(my_new_list[1:3])  # Elementos del índice 1 al 2


# ------------------------------------------
# 2. TUPLAS (tuple)
# ------------------------------------------
# Una tupla es una estructura de datos ordenada e INMUTABLE (no se puede modificar).

# Definición de tuplas
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (30, 60, 30)

print(my_tuple)
print(type(my_tuple))  # <class 'tuple'>

# Acceso a elementos e índices
print(my_tuple[0])   # 35
print(my_tuple[-1])  # "Brais"

# Métodos principales de Tuplas

# count: Cuenta cuántas veces aparece un elemento
print(my_tuple.count("Brais"))  # 2

# index: Devuelve el índice de la primera aparición de un elemento
print(my_tuple.index("Moure"))  # 3
print(my_tuple.index("Brais"))  # 2

# Inmutabilidad (Descomentar para probar el error)
# my_tuple[1] = 1.80  # TypeError: 'tuple' object does not support item assignment
# my_tuple.append("Dev")  # AttributeError: 'tuple' object has no attribute 'append'

# Suma / Concatenación de tuplas (crea una nueva tupla)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas (Slicing)
print(my_sum_tuple[3:6])

# Conversión entre Tuplas y Listas (para modificar una tupla)
my_tuple_list = list(my_tuple)  # Convertir a lista (mutable)
my_tuple_list[4] = "MoureDev"
my_tuple_list.insert(1, "Azul")
my_tuple = tuple(my_tuple_list)  # Convertir de nuevo a tupla (inmutable)
print(my_tuple)
print(type(my_tuple))  # <class 'tuple'>

# Eliminación de una tupla
# del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion
del my_tuple  # Elimina la variable por completo
# print(my_tuple)  # NameError: name 'my_tuple' is not defined

