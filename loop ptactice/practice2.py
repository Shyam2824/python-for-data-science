# check the number is perfect 
number= eval(input("Enter the number:- "))
total=0

for n in range(1,number):
    if number%n==0:
        total= total+n
    
print("total:= ",total)

if total== number:
    print("Perfect number")
else:
    print("not perfect number")