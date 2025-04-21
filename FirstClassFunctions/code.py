# First-Class Functions in Python

# 1. Functions are treated as first-class citizens in Python.
#    This means that functions can be assigned to variables, passed as arguments to other functions,
#    and returned as values from other functions.

# 2. Assigning a function to a variable:
#    You can assign a function to a variable and call it using that variable.

# 3. Passing functions as arguments:
#    Functions can be passed as arguments to other functions, allowing for higher-order functions.

# 4. Returning functions from other functions:
#    Functions can return other functions, enabling the creation of closures and decorators.

# 5. Storing functions in data structures:
#    Functions can be stored in lists, dictionaries, or other data structures for dynamic execution.

# Example usage of first-class functions will demonstrate these concepts.



def divide(dividend, divisor):
    if divisor==0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return dividend/divisor

def calculate(*values,operator):
    return operator(*values)
print(calculate(4,2,operator=divide))         #divide is function passed as argument. Thats first class function

#another example

def search(sequence, expected,finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find the element with {expected}")

friends =[
    {"name":"Rolf","age":23},
    {"name":"Tom","age":26},
    {"name":"Jim", "age":29}
]

def search_name(name):
    return name["name"]


print(search(friends,"Tom",finder=search_name))
try:
    print(search(friends,"Jim",finder=search_name))
except RuntimeError as e:
    print(e)
finally:
    print("This is the end")
  