# Simple Method

class Student:
    
    def __init__(self,name):
        self.name=name
    
    def Study(self):
        print("I study properly",self.name)
name= input("Enter name")
s1 = Student(name)
s1.Study()