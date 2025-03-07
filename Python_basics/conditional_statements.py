#Conditions are used to run a block of code only if the condition is true or false

day_of_week = input("What day of the week is it today? ").lower() #.lower() is used to convert the input to lower case

if day_of_week == "monday":
    print("It's Monday, the start of the week")
elif day_of_week == "tuesday":
    print("It's Tuesday, the second day of the week")
else:
    print("It's not Monday or Tuesday. Have a great day!")


#Remember that if comes first and then elif and then else
#If the condition is true then the block of code under that condition will run and the rest will be skipped
#any statement out of indentation will not be considered as part of the if block. That code will run anyways

print("This is outside the if block and will run anyways")