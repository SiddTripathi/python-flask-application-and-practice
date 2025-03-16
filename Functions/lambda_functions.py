#lambda functions are anonymous functions that are defined using the lambda keyword
#lambda functions can have any number of arguments but only one expression
#lambda functions are used when a small function is needed for a short period of time
#lambda functions are used in combination with functions like map(), filter(), reduce()
#lambda functions can be assigned to a variable and used like a normal function


def add(a,b):
    return a+b

#now lambda of the above function
add_lambda = lambda a,b: a+b
print(add_lambda(2,3))

#using lambda with map()
#map() function is used to apply a function to all the elements in a list
#map() function takes two arguments - a function and a list

numbers = [1,2,3,4,5]
squared = list(map(lambda x: x*x, numbers)) #squares all the numbers in the list. The lambda function x*x is applied to all the elements in the list.
                                            # The map() function returns a map object which is converted to a list using list() function
print(squared)

#In python, mostly people use list comprehension instead of map() function
squared = [x*x for x in numbers]
print(squared) #Lambda functions can be used with list comprehension as well but are not recommended

#double function on list using list comprehension
def double(x):
    return x*2

doubled = [double(x) for x in numbers] #doubles all the numbers in the list. The double() function is applied to all the elements in the list.
print(doubled)