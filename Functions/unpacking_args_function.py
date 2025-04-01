#in function args, * is used to unpack the arguments
# *args is used to unpack the positional arguments
# **kwargs is used to unpack the keyword arguments

#example




def add_num(x,y):
    return x+y

numbers = [2,3]
print(add_num(*numbers)) #unpacking the list numbers. 2 is passed to x and 3 is passed to y


#example 2
def multiply_num(*args):
    print(f"This is multiply args{args}") #args is a tuple. *args unpacks the arguments and stores them in a tuple
    total = 1
    for num in args:
        total *= num
    return total

print(multiply_num(2,3,4,5)) #2,3,4,5 are passed as arguments. *args unpacks the arguments and stores them in a tuple

#example 3 - unpacking dictionary

def add_dict(a,b):
    return a+b

numbers = {'a': 2, 'b': 3} #keys of dictionary and arguments of function should match otherwise it will throw an error
print(add_dict(**numbers)) #unpacking the dictionary numbers **. 2 is passed to a and 3 is passed to b 

def apply(*args, operator):
    print(f"This is apply args{args}") 
    if operator == '*':
        return multiply_num(*args) #unpacking the tuple args. if *args is not unpacked, it will return the tuple instead of the result
    elif operator == '+':
        return sum(args)
    else:
        return "Invalid operator"
    
print(apply(3,2,1, operator='*')) 

#Unpacking keyword arguments

def named(**kwargs):
    print(kwargs)

named(name='John', age=25, city='New York') #kwargs unpacks the keyword arguments and stores them in a dictionary

#similarly, we can unpack the dictionary and pass it as keyword arguments

def named_again(name, age):
    print(name, age)

details = {'name': 'John', 'age': 25}
named_again(**details) #unpacking the dictionary details and passing it as keyword arguments

named(**details) #unpacking the dictionary details and passing it as keyword arguments to named function