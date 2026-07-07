## Mobile Class

class Mobile:
    
    def __init__(self, brand , color, ram, storage):
        self.brand= brand
        self.color= color
        self.ram= ram
        self.storage = storage
    
    def display(self):
        print("Brand of my phone: ", self.brand)
        print("Colour of my phone: ", self.color)
        print("Ram of my phone: ", self.ram)
        print("Storage of my phone: ", self.storage)
    
    
brand= input(" Enter your phone Brand: ")
color= input(" Enter your phone Colour: ")
ram= input(" Enter your phone Ram: ")
storage= input(" Enter your phone Storage: ")

d1= Mobile(brand,color,ram,storage,)
d1.display()