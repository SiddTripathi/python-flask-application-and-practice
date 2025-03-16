#A dictionary comprehension is similar to list comprehension but here we are dealing with key value pairs instead of single elements.

#Syntax:
# {key: value for key, value in iterable}

user_details = [
    (1,'John', 'john`123'),
    (2,'Smith', 'smith@123'),
    (3,'Peter', 'peter#123')
]

#Create a dicitonary with name as key and tuple as value
user_details_mapping ={user[1]: user for user in user_details}
print(user_details_mapping)

#by doing this we can easily access the user details by name. Otherwise we have to iterate through the list to get the user details by name.

print(user_details_mapping['John']) #Output: (1, 'John', 'john`123')

username_input = input('Enter the username: ')
username_password = input('Enter the password: ')

_, username, password = user_details_mapping[username_input] # _ is used to ignore the first element of the tuple. Tuple unpacked to get the username and password. id not used here.
if password == username_password:
    print('Login successful')
else:
    print('Login failed')

#exercise
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.

student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}
# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list

def average_grade_all_students(students_list):  
    total = 0
    count = 0
    for student in students_list:
        total += sum(student['grades']) #sum of tuple containing all the grades of a student
        count += len(student['grades'])
    return total / count