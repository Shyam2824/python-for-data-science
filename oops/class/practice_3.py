# Instance Variable ==> Unique value of every variable

class Student:
    def __init__(self, name, roll):
        self.name= name
        self.roll= roll
        
s1= Student("Rahul", 258)
s2= Student("Mohan", 658)

print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll)