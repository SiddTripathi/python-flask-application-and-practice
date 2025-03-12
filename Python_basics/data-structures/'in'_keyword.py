#The 'in' keyword in python is used to check if a value is present in a list, tuple or set or not
# It can also be used to check if a key is present in a string (sub-string) or dictionary


fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
cars_tuple = ("BMW", "Audi", "Mercedes", "Toyota", "Honda")
cities_set = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"}

#check if a value is present in a list
fruit_user = input("Enter a fruit name: ")
if fruit_user in fruit_list:
    print(f"{fruit_user} is present in the list")
else:
    print(f"{fruit_user} is not present in the list")

#check if a value is present in a tuple
car_user = input("Enter a car name: ")
if car_user in cars_tuple:
    print(f"{car_user} is present in the tuple")
else:
    print(f"{car_user} is not present in the tuple")

#check if a value is present in a set
city_user = input("Enter a city name: ")
if city_user in cities_set:
    print(f"{city_user} is present in the set")
else:
    print(f"{city_user} is not present in the set")


print(abs(-1) in [1, 2, 3]) #abs(-1) will return 1 and 1 is present in the list so it will return True