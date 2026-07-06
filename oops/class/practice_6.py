# Question

# Create a Car class.

# Take input:

# Brand
# Model
# Price

# Print the car details.

class Car:
    def __init__(self,Brand, Model, price, Milage, color):
        self.Brand=Brand
        self.Model=Model
        self.price=price
        self.Milage=Milage
        self.color=color
        
Brand= input("Enter the Brand name: ")
Model= input("Enter the Model name: ")
price= input("Enter the Price name: ")
Milage= input("Enter the Milage name: ")
color= input("Enter the Colour name: ")

C1= Car(Brand,Model,price,Milage,color)

print("\n Car details : ")
print("Enter your car Brand : ", Brand )
print("Enter your car Model : ", Model )
print("Enter your car price: ",price )
print("Enter your car Milage : ", Milage )
print("Enter your car Colour : ", color )