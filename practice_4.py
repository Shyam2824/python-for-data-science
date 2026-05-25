# swap two variable
 #with generating extra variable
 
num_1= eval(input("Enter the first number: "))
num_2= eval(input("Enter the second number: "))

temp= num_1
num_1= num_2
num_2= temp

# without using extra variable

num_1= num_1+ num_2
num_2= num_1-num_2
num_1= num_1-num_2

print(f"the num1 : {num_1} and num2 {num_2}")