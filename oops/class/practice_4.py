# Question

# Create a Student class.

# Take input from the user:

# Roll Number
# Name
# Age

# Create an object and print all the details.

class Student:
    def __init__(self,roll_no, name,age):
        self.roll_no= roll_no
        self.name= name
        self.age= age
    
roll_no= int(input("Enter your roll. : "))
name= input("Enter your Name : ")
age= eval(input("Enter your age : "))

s1= Student(roll_no, name,age)

print("\n Student details")
print("Name: ", s1.name)
print("Age: ", s1.age)
print("Roll : ", s1.roll_no)