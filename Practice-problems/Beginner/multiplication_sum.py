"""
Given two integer numbers, 
write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

"""

def calculate_sum_product(num1: int, num2: int):
    if num1*num2<=1000:
        return f"Product is less than 1000 and its {num1*num2}"
    else:
        return f"Product>1000. Sum = {num1+num2}"
    

num1 = int(input("Enter the first number - "))
num2 = int(input("Enter the Second number - "))

print(calculate_sum_product(num1,num2))
