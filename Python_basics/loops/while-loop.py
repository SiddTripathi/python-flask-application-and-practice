#while loop in python
#while loop is used to execute a block of code multiple times as long as the condition is true

#number guess game

number = 7

while True:
    user_input = input("Would you like to play the number guess game? (y/n): ").lower()
    if user_input == 'n':
        break  #break is used to exit the loop
    elif user_input == 'y':
        user_number = int(input("Enter a number between 1 to 10: "))
        if user_number == number:
            print("You guessed it right!")
        else:
            print("You guessed it wrong!")
    else:
        print("Invalid input. Please enter y or n")
print("Game over!")
