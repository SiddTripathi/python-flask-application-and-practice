# __str__ is used to define a string representation of an object
# # __repr__ is used to define a string representation of an object that can be used to recreate the object.
# # It is often used for debugging purposes.
# __repr__ is unambiguous meaning it should be clear what the object is, while __str__ is more user-friendly and meant for end-users.

#both these are for debugging purposes and are not used in production code.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # User-friendly string representation of the object
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):  # Unambiguous string representation of the object
        return f"Person(name='{self.name}', age={self.age})"
    

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1)  # Output: Name: Alice, Age: 25
print(person2)  # Output: Name: Bob, Age: 30
print(repr(person1))  # Output: Person(name='Alice', age=25)
print(repr(person2))  # Output: Person(name='Bob', age=30)


#Exercise
class Store:
    def __init__(self,name):
        self.name = name
        self.items = []
    def add_item(self, name, price):
        item = {
            'name': name,
            'price': price
        }
        self.items.append(item)
    def stock_price(self):
        total_price = sum(item['price'] for item in self.items)
        return total_price

        