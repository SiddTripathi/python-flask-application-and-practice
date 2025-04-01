#Object oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the 
# form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). 
# OOP languages include Python, Java, C++, Ruby, and many others.
# OOP is a way to structure your code so that it is more organized, reusable, and easier to maintain. It allows you to create classes 
# that define the properties and behaviors of objects, and then create instances of those classes to represent specific objects in your program.


#Without OOP

student = {
    'name': 'John Doe',
    'age': 20,
    'grade': (23, 45, 67, 89, 90)
}

def calculate_average_grade(student):
    grades = student['grade']
    return sum(grades) / len(grades)
print(f"Average Calculated without OOP{calculate_average_grade(student)}") # Output: 62.8
#In this example, we have a dictionary representing a student, and a function that calculates the average grade of that student.

#With OOP
class Student:
    def __init__(self):              # Constructor method to initialize the object. Called when an instance of the class is created.
                                     # The self parameter is a reference to the current instance of the class. It allows you to access instance variables and methods.
        self.name = "John Doe"
        self.age = 20
        self.grades = (23, 45, 67, 89, 90)

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student = Student()                #name, age, and grades are instance variables. They are unique to each instance of the class. Properties of the class.
print(f"Average calculated form OOP concept{student.calculate_average_grade()}") # Output: 62.8

# student.Calculate_average_grade() is similar to Student.calculate_average_grade(student). However, python allows you to call the 
# method without passing the instance as an argument. Thats the use of self parameter.
# The instance is automatically passed as the first argument to the method when it is called on the instance.

#Example two - Passing arguments to the constructor
# constructor method that takes two arguments: name and age.

class Person:
    def __init__(self, name, age): # Constructor method to initialize the object. Called when an instance of the class is created.
        self.name = name            # name and age are instance variables. They are unique to each instance of the class.
        self.age = age

    def greet(self):              
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") 


person1 = Person("Alice", 25)      
person2 = Person("Bob", 30)       

person1.greet()               
person2.greet()                 