# ------------------------------------------
#functions
# ------------------------------------------
def sum_numbers(num1,num2=10):
    return num1+num2

#ejecution
num1=input("Enter first number: ")
num2=input("Enter second number: ")
result = sum_numbers(int(num1), int(num2))
print("The sum is:", result)

#with default value
print(sum_numbers(5))

# ------------------------------------------
#*args and **kwargs
# ------------------------------------------

#*args
def my_function(*args):
    for i in args:
        print(i)
    print(*args)#convert dates in a tuple
my_function(1,2,4,2,1.4)

#**kwargs  
    
def empleado(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
empleado(nombre="juan", apellido="rodriguez")