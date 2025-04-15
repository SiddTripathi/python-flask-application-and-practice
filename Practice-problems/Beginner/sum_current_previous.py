"""
Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

"""


def sum_current_previous_num(range_num: int)->list:
    fibonaci_list = []
    for i in range(range_num):
        if i==0:
            current_number = i
            previous_number = 0
            summ = current_number+previous_number
            fibonaci_list.append(summ)

            print(f"Current Number {current_number} Previous Number {previous_number} Sum = {summ}")
        else:
            current_number = i
            previous_number = i-1
            summ = current_number+previous_number
            fibonaci_list.append(summ)
            print(f"Current Number {current_number} Previous Number {previous_number} Sum = {summ}") 
    print(fibonaci_list)
        



sum_current_previous_num(10)