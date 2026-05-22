# Write a python program to do arithmetical operator

 # Addition

num_1= eval(input("Enter the number 1 : "))
num_2= eval(input("Enter the number 2 : "))

total_number = num_1+ num_2

print(f"sum: {num_1} + {num_2} = {total_number}" ) # f used for formatting
print(type(num_1))

## Division

if num_2==0:
    print("Number is not divided")
else:
    result= num_1/ num_2
    print(f"result: {num_1} / {num_2} = {result}")