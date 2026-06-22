# while loop 
l_num= -555

num= eval(input("Enter the number: "))

while num!= -1:
    if num> l_num:
        l_num = num
    num= eval(input("Enter the number again:"))

print("Largest number: ", l_num)