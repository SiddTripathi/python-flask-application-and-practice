#boolean is used to check if the condition is true or false

print(10 > 9)
print(10 == 9)
print(10 < 9)


#even strings can be compared using boolean or list

#however while comparing lists keep in mind that items in list same will return true but 'is' will return false
#is is used to check if the objects are same or not
# == is used to check if the values are same or not

list1 = ["apple", "banana"]
list2 = ["apple", "banana"]

print(f"The '==' compares values - {list1 == list2}")
print(f"The 'is' is used to compare if objects are same or not - {list1 is list2}")

#if we do list1 assign list2 then both will point to same object and hence 'is' will return true
list1 = list2
print(f"The 'is' is used to compare if objects are same or not - {list1 is list2}")
