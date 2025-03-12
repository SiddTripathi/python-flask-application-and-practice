#dictionaries are key value pairs. You can use a key to access a value.
#dictionaries are mutable. Dictionaries are unordered.
#dictionaries are enclosed in curly braces.


#creating a dictionary
my_dict = {'name':'Max','age':28,'city':'New York'}
print(my_dict)

#accessing values
value = my_dict['name'] #Like lists, you can access values but instead of using an index, you use a key.
print(value)

#adding a key value pair
my_dict['email'] = 'max@gmail.com'
print(my_dict)

#deleting a key value pair
del my_dict['email']
print(my_dict)


#list of dictionaries
employees = [
    {'name':'Max','age':28},
    {'name':'Lisa','age':35},
    {'name':'John','age':45}  #list of dictionaries
]

#accessing values
print(employees[1]['name']) #accessing the name of the second employee using the index of the list and the key of the dictionary.



#How to iterate over a dictionary

student_marks = {'Tom': 70, 'Jim': 80, 'Sue': 85}

for name in student_marks:
    print(f'Student name - {name} got {student_marks[name]}') #prints the keys

#more efficient way to iterate over a dictionary
for name, marks in student_marks.items():  #items() method returns a view object that displays a list of a dictionary's key-value tuple pairs. Here we are unpacking the key value pairs.
    print(f'Student name - {name} got {marks}') #key is name and value is marks in for loop


#using the in operator to check if a key exists in a dictionary

if 'Tom' in student_marks:
    print('Tom is in the dictionary')
else:
    print('Tom is not in the dictionary')

#using just the values of a dictionary
for marks in student_marks.values():
    print(f'Marks of students {marks}')

average_marks = sum(student_marks.values())/len(student_marks)
print(f'The average marks of the students is {average_marks}')