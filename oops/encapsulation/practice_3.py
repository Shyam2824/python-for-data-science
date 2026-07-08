#  Protected   Member 

class Car:
    def __init__(self, brand, model, engine):
        self.brand= brand  # public attribute
        self._model= model # protected attributed
        self._engine = engine #protected attributed
        
    # Protected Method
    def _car_details(self):
        print(f"Brand : {self.brand} , Model of : {self._model}, Engine: {self._engine} ")
        
class Electric_car(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model,"Electric")
        self._battery_capacity= battery_capacity
        
    def show_info(self):
        self._car_details()  # Accessing protected method from subclass
        print(f"Battery: {self._battery_capacity}KWh")
        
        
c1= Electric_car("TATA", "Punch", 500)

c1.show_info()