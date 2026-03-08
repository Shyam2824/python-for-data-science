#find the length of the string without using the len() function

s= input("Enter String : ")
counter = 0

for i in s:
    counter+=1
print("length of string : ", counter)



#get user name in the email
s= input("enter the email")
position=s.index('@')
print(s[0:position])