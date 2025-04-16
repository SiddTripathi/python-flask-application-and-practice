#Sometimes you need to put a nice error message which is relevant for users to understand.  Exception handling and error handling

#example
def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend/divisor


students = [
    {"name":"Rom","grades":[20,40,10]},
    {"name":"Dom","grades":[20,10,50]},
    {"name":"Tom","grades":[50]},
    {"name":"Bom","grades":[10,10,20]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        avg = divide(sum(grades),len(grades))
        print(f"{name} has average grades {avg}")
except ZeroDivisionError as e:
    print(f"{name} does not have any grades yet")     #If any error (like zero Division error is encountered)

else:
    print("All students average calculated")          #this runs when all try things succedded no error
finally: 
    print("Thanks !!!!")                              #finally runs anyways no matter what