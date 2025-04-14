#type hinting in python is used to hint about the type of parameter a function can take and the type of value it returns.


def average(numbers: list[float]) -> float:            # This is a type hinting example
    """
    Calculate the average of a list of numbers.
    
    :param numbers: A list of float numbers
    :return: The average of the numbers as a float
    """
    return sum(numbers) / len(numbers) if numbers else 0.0

print(average([1.0, 2.0, 3.0]))  # Output: 2.0
