#class method is method that is bound to the class and not the instance of the class. 
# It can be called on the class itself, rather than on an instance of the class. No need to create class instance to call the class method.

#instance method is a method that is bound to the instance of the class.


# It is defined using the @staticmethod decorator.
# Static methods are used when you want to define a method that does not depend on the instance or class variables.
# They are similar to regular functions but are defined within the class for organizational purposes.


from calendar import c

from regex import B


class ClassTest:
    def instance_method(self):              # self is a reference to the instance of the class.
        print("This is an instance method.")

    @classmethod
    def class_method(cls):               # cls is a reference to the class itself, not the instance.
        print("This is a class method.")
        print(f"Class name: {cls.__name__}")
    
    @staticmethod
    def static_method():              # No self or cls parameter is required.
        print("This is a static method.")



# Create an instance of the class
test_instance = ClassTest()
test_instance.instance_method()  
test_instance.class_method()  
ClassTest.class_method()  
test_instance.static_method() 
ClassTest.static_method()  
# # The instance method can access instance variables and methods, while the class method can access class variables and methods.


#lets see an example of class method and static method

class Book:
    TYPES = ("hardcover", "paperback")  # Class variable
    # Class variable is shared among all instances of the class.
    def __init__(self,tittle,book_type,weight):
        self.tittle = tittle
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book(tittle={self.tittle}, book_type={self.book_type}, weight={self.weight})"
    # __repr__ is used to define a string representation of an object that can be used to recreate the object.

    @classmethod
    def is_hardcover(cls, name, page_weight):  # Class method
        return cls(name, cls.TYPES[0], page_weight+100)  # Create a hardcover book instance
    
    @classmethod
    def is_paperback(cls, name, page_weight):  # Class method
        return cls(name, cls.TYPES[1], page_weight)  # Create a paperback book instance


book1 = Book.is_hardcover("Python Programming", 500)
book2 = Book.is_paperback("Java Programming", 300)
print(book1)
print(book2)

#exercise
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
    
    def __repr__(self):
        return f"Store(name={self.name}, items={self.items})"

    @classmethod
    def franchise(cls,store):
        return cls(store.name +" - Franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"
    

store1 = Store("Store 1")
store1.add_item("item1", 10)
print(Store.franchise(Store('Amazon')).name) #.name # Accessing the name attribute of the Store instance created by the franchise class method.

# Creates a new Store instance with name "Amazon", passes it to the franchise method,
# which returns a new Store instance with name "Amazon - Franchise", and prints its name.