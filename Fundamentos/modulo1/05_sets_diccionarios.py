#SETS
my_set = {}
print(type(my_set))

my_set = {'phyton','java','c'}
print(type(my_set))

my_set.add('java')
print(my_set)

my_set.add('javascript')
print(my_set)

my_set_0 = {'phyton','java','c'}
my_set.difference_update(my_set_0)
print(my_set)

