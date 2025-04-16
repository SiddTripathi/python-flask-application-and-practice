#lets understand about importing in python 
"""
This module demonstrates the concept of importing in Python.

Importing in Python allows you to reuse code from other modules or libraries by bringing their functionality into your current script. 
It helps in organizing code, avoiding redundancy, and leveraging pre-built libraries for efficient development.

The special variable `__name__` in Python is used to determine whether a module is being run as the main program or being imported into another module. 
When a module is run directly, `__name__` is set to `"__main__"`. This allows you to write code that executes only when the module is run directly, 
and not when it is imported elsewhere.
"""

def divide(dividend, divisor):
    return dividend/divisor


print("mymodule.py:", __name__) #using __name__ function. __name_ will be __main__ if same file run. But if called by another module, __main__ will
                                #print the path how the module imported