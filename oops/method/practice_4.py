# Multiple method
class Mobile:
    def __init__(self,brand):
        self.brand= brand
        
    def turn_on(self):
        print(self.brand, "turn on ")
        
    def turn_off(self):
        print(self.brand, "turn off ")
        
m1= Mobile("Real me")

m1.turn_on()
m1.turn_off()