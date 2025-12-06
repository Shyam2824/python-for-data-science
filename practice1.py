#Consider an array as array1 consisting of n number of elements. Replace all the negative values 
# present in the array with X. Provided the value of X is 0 and print the resultant output.

n = int(input("Enter the number of element"))
array1= []

print("Enter the number")
for i in range(n):
    array1.append(int(input()))
    
#replacing negative value


for i in range(n):
    if array1[i]<0:
        array1[i]=0
        
print("Solved array:", array1)