# Multiple Object

class Student:
    def __init__(self, name, roll, section): # constructor
        self.name= name
        self.roll= roll
        self.section= section
        
    def display(self): # method
        print("=============================")
        print("Name :", self.name)
        print("Roll : ", self.roll)
        print("Section : ", self.section)
        
n=int(input("Enter the number of students: ")) # o of student

students =[]
for i in range(n):
    print(f" Students {i+1}") # no of student count
    # get user input
    name= input("Name : ")
    roll= int(input("Roll : "))
    section= input("Section : ")
    
    s1=Student(name,roll, section) # call class
    
    students.append(s1)
    
    print("\n Student details ")
    
for j in students:
    j.display() # call function