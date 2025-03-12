#Program to create a list of even numbers from list of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is an even number")
        even_numbers.append(number)
print(f"List of even numbers is {even_numbers}")

user_input = input("Enter your choice (a/q): ")

if user_input == 'a':
    print("Add")
elif user_input == 'q':
    print("Quit")