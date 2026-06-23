# find odd or even using while loop
number= eval(input("Enter the number :- "))
odd_num=0
even_num=0

while number !=0:
    if number%2 ==0:
        even_num += 1
    
    else:
        odd_num += 1
        
    number= eval(input("Enter 0 to stop the loop:= "))
    
print ("Odd number : ", odd_num)
print ("Even number : ", even_num)
    