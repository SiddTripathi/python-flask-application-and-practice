#parameters or arguments in function are used to pass values to the function
#parameters are defined in the function definition
#arguments are the values passed to the function

def sum_num(a,b):
    return a+b

print(f"The sum of numbers is {sum_num(2,3)}") #2 and 3 are arguments
# here 2 and 3 are passed to the function sum_num as arguments a and b
# 2, 3 are positional arguments so they are passed in the same order as the parameters in the function definition

#keyword arguments
#arguments can be passed by using the parameter names in the function call. This way the order of the arguments does not matter and its easier to understand the function call

def divide_num(dividend, divisor):
    if divisor == 0:
        return "Cannot divide by zero"
    else:
        return dividend/divisor
    
print(f"The result of division is {divide_num(divisor=2, dividend=4)}") #2 and 4 are passed as keyword arguments\

#Note - positional arguments should be passed before keyword arguments. If keyword arguments are passed before positional arguments, it will throw an error

#Default arguments. Default arguments are used when the function is called without passing the argument. The default value is used in that case

def name_age(name, age=25):
    return f"Name is {name} and age is {age}"

print(name_age("John")) #age is not passed so default value 25 is used. 

#Note - default arguments should be at the end of the parameter list. If default arguments are placed before non-default arguments, it will throw an error
# def name_age(age=25, name): #this will throw an error