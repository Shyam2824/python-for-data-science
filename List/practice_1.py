# use append and insert

# Create a list
numbers = []

# Input number of elements
n = int(input("How many numbers do you want to enter? "))

# Add numbers to the list
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\nList:", numbers)
print("Length:", len(numbers))

# Append a new number
new_num = int(input("\nEnter number to append: "))
numbers.append(new_num)

print("After append:", numbers)
print("Length:", len(numbers))

# Insert a number
position = int(input("\nEnter position to insert: "))
value = int(input("Enter value to insert: "))
numbers.insert(position, value)

print("After insert:", numbers)
print("Length:", len(numbers))