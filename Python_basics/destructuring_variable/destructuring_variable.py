#lets understand destructuring variable in python with example
# Destructuring variable is a way to unpack the values from a list, tuple, or dictionary into variables.

#simple example of destructuring variable
a, b = 1, 2 # a=1, b=2
print(a)
print(b)

#similarly we can unpack the values from a dictionary
dict1 = {'name':'John', 'age':25}

for key, value in dict1.items():  #.items() method returns a view object that displays a list of a dictionary's key-value tuple pairs and this tuple pairs can be unpacked into key and value
    print(key, value)

#unpacking values from a list
#As you can see, the list contains tuples, and each tuple contains three elements. We can unpack these elements into three variables using destructuring assignment.
list1 = [('Tom',25,'Mechanical'), ('John', 22, 'Electrical'), ('Harry', 30, 'Civil')] 
for name, age, branch in list1:
    print(name, age, branch)

#unpacking values from a tuple when we want to ignore some values
tuple1 = ('Tom', 25, 'Mechanical')
name, _, branch = tuple1 #we can use _ to ignore the values as per python convention
print(name, branch)


#using * to unpack the remaining values
#In Python, you can use the * operator to unpack the remaining values into a list.

num_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, *c = num_list1
print(a)  #a=1
print(b)  #b=2  
print(c) #c will be a list containing the remaining values

#similarly

*a,b= num_list1
print(a) #a will be a list containing the remaining values
print(b) #b=9