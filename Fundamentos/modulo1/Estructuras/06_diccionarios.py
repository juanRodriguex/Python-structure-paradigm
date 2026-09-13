#DICTIONARIES

my_dict = {'Nombre':'juan',
           'Apellido':'rodriguez'}
print(type(my_dict))
print(my_dict['Nombre'])
print(my_dict.values())
print(my_dict.keys())

my_dict= tuple(my_dict.values())
print(my_dict)