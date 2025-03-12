#for loop in python
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects
# for loop can be used to execute a block of code multiple times for each item in the sequence


list_of_students = ["John", "Mike", "Sara", "Tom", "Jerry"]
i = 0
for student in list_of_students:
    
    print(f"Student number {i + 1} is {student}")
    print("Hello " + student)
    i += 1


#in-built functions to get sum and length of a list without using for loop

#sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
sum = sum(numbers)
print(f"The sum of numbers in the list is {sum}")


#length of a list
print(f"The length of the list is {len(numbers)}")