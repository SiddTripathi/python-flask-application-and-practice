#List, Tuples and Sets in Python


#list
courses_lists = ['History', 'Math', 'Physics', 'CompSci']

#tuple
courses_tuple = ('History', 'Math', 'Physics', 'CompSci')

#difference between list and tuple is that list is mutable and tuple is immutable meaning you can't change the values in tuple but you can in list


#sets
courses_sets = {'History', 'Math', 'Physics', 'CompSci'}
#difference between sets and list is that sets don't have any order and you can't access them by index
#sets are used to remove duplicates from a list
#to create an empty set you have to use set() function


#items in list and tuple can be accessed by index
print(f"This is printed by list {courses_lists[0]}") #prints first item in the list as index starts from 0

print(f"This is printed by Tuple {courses_tuple[0]}") #prints first item in the tuple as index starts from 0


#add items to list
courses_lists.append('Art')

#remove items from list
courses_lists.remove('Math')

#add items to sets
courses_sets.add('Computer Science')

#remove items from sets
courses_sets.remove('Math')

#You can't add items to tuple as it is immutable and not remove items from tuple
#to access items in sets you have to use for loop
for course in courses_sets:
    print(course)