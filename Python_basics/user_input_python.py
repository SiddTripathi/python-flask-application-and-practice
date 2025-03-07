#To take input from user we use input() function in python
#input() function always returns a string

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age+2} years old.")

#We can also format output to decimal places using f string

size_input = int(input("Enter the size of the room in square feet: "))
square_meters = size_input / 10.8
print(f"The size of the room is {size_input} square feet or {square_meters:.2f} square meters.") #.2f is used to format the output to 2 decimal places
