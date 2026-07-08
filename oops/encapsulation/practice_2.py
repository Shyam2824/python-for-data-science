# Public Encapsulation

class Car:
    def __init__(self, brand, color):
        self.brand= brand
        self.color= color
        
    def display(self):
        print(f"Car: {self.brand} and {self.color}" )
        
# Creating Object
car= Car("Toyota", "Corolla")

# Accessing public member

print(car.brand)
print(car.color)

car.display()