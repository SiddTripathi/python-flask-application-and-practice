#string formatting is to put dynamic information in a string
# %s is a placeholder for a string

name = "John"
greetings = "Hello, %s!"
print(greetings % name)

name = "Ravi"
greetings = "Hello, %s!"
print(greetings % name)

# %d is a placeholder for a number
age = 23
years = "I'm %d years old"
print(years % age)

age = 45
years = "I'm %d years old"
print(years % age)


#another way to format strings is to use the format method
# {} is a placeholder for a string

#.format() method is used to format the string
name = "Ram"
greetings = "Hello, {}!"
print(greetings.format(name))

another_example = "Hello, {}. You are {} years old."
print(another_example.format(name, age))


#f string is another way to format strings --> generally used in python 3.6 and above
name = "Ronny"
greetings = f"Hello, {name}!"
print(greetings)