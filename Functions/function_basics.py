#functions in python are code blocks that are executed when they are called or invoked.
#Functions are defined using the def keyword followed by the function name and parentheses ().

#basic syntax of function

def Hello():
    print('Hello World')

#calling the function
Hello()

print('\n \n')


#similarly another example
def age_in_months_func():
    user_age = int(input('Enter your age: '))
    age_in_months = user_age * 12
    print(f'Your age in months is {age_in_months}')


print('Welcome to the age in months calculator')
age_in_months_func()
print('Thank you for using the age in months calculator')