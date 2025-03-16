#The return statement is used to return a value from the function. The value returned by the function can be stored in a variable or used directly in the code.
#The return statement is the last statement in the function. Any code after the return statement is not executed.
#The return statement can return multiple values separated by commas. The values are returned as a tuple.

#by default, a function returns None if no return statement is used. None is a special value in Python that represents the absence of a value.


from numpy import divide


def add_sub(a,b):
    return a+b, a-b

sum_num, difference = add_sub(5,3) #here we are unpacking the tuple returned by the function add_sub. Destructoring the tuple
print(f"The sum of two number is {sum_num} and the difference is {difference}")
#The function add_sub returns two values - sum and difference of the numbers. The values are returned as a tuple. The tuple is stored in the variable result.


def divide_mul(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a/b, a*b
    
divide, multiply = divide_mul(6,2)
print(f"The division of two numbers is {divide} and the multiplication is {multiply}")
#The function divide_mul returns two values - division and multiplication of the numbers. There are two return statements in function but only one is executed. The code after the return statement is not executed.

#exercise
def return_42():
    return 42

def my_function(x, y):
    return x * y

mult = my_function(3, 5)
print(mult)