#the list comprehension is a more concise way to write the same code
#List comprehension is a way to create a new list by iterating over an existing list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"List of even numbers is {even_numbers}")

#similarly we can create a list of squares of numbers
numbers2 = [2,4,6,8]    #list of numbers
squares = [number*number for number in numbers2]  #list comprehension
print(f"List of squares is {squares}")

#if we want to do same thing using for loop
squares2 = []
for number in numbers2:
    squares2.append(number*number)  #appending the square of number to the list
print(f"List of squares using for loop is {squares2}")  #printing the list of squares


# List comprehension with if else
#syntax: [expression for item in list if condition]

#Example: create a list of names which start with 'S'

names = ['Sachin', 'Rahul', 'Sourav', 'Virat', 'Rohit', 'Shikhar']

#using for loop
names_starting_with_S = []
for name in names:
    if name.startswith('S'):
        names_starting_with_S.append(name)

print(f"List of names starting with 'S' using for loop is {names_starting_with_S}")

#using list comprehension
names_starting_with_S = [name for name in names if name.startswith('S')]

print(f"List of names starting with 'S' using list comprehension is {names_starting_with_S}")

#Hence list comprehension is a more concise way to write the same code