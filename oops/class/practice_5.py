# Question

# Create an Employee class.

# Take input:

# Employee ID
# Employee Name
# Salary

# Print the employee details.

class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id= emp_id
        self.emp_name= emp_name
        self.salary= salary
        
emp_id= int(input("Enter your employee Id : "))
emp_name= input("Enter your employee Name : ")
salary= int(input("Enter your Salary : "))

E1= Employee(emp_id, emp_name, salary)

print(" Employee Details: ")
print("Employee Id: " ,E1.emp_id)
print("Employee name: ", E1.emp_name)
print("Employee Salary: ", E1.salary)