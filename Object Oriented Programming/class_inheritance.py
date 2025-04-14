#inheritance allows us to define a class that inherits all the methods and properties from another class

class Device:
    def __init__(self, name, connection_type):
        self.name = name
        self.connection_type = connection_type
        self.connected = True
    
    def __str__(self):
        return f"{self.name!r} ({self.connection_type})"
    def disconnect(self):
        self.connected = False
        print(f"disconnected.")


class Printer(Device):
    def __init__(self, name, connection_type, page_count):
        super().__init__(name, connection_type)  # Call the constructor of the parent class
        self.page_count = page_count
        self.remaining_pages = page_count
    
    def __str__(self):
        return super().__str__() + f" with {self.remaining_pages} pages remaining."  #super() is used to call the method of the parent class.
     
    def print_page(self,pages):
        if not self.connected:
            print("Printer is not connected.")
            return
        print(f"Printing ... {pages} pages .")
        self.remaining_pages -= pages





printer = Device("Printer", "USB")

print(printer)
printer.disconnect()

printer1 = Printer("Printer1", "USB", 100)
printer1.print_page(35)
print(printer1)
printer1.disconnect()         #Object of the child class can access the methods of the parent class.