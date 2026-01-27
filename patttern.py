#create 6 * 

n= int(input("Enter no of star: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    
### factorial divide
n= int(input("Enter the number : "))

fact=1
result=0
for i in range(1,n+1):
    fact= fact*i
    result=result+i/fact
print("result:  ", result)