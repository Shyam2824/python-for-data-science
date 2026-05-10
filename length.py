# #find the length of the string without using the len() function

# s= input("Enter String : ")
# counter = 0

# for i in s:
#     counter+=1
# print("length of string : ", counter)



# #get user name in the email
# s= input("enter the email")
# position=s.index('@')
# print(s[0:position])


# #count the frequency of the string

# s= input("enter the string: ")
# term= input("enter the word ")

# count=0

# for i in s:
#    if i== term:
#     count+=1
    
# print("frequency ", count)

# remove particular words in string


s= input("enter the string: ")
term= input("enter the remove words ")
result= ""

for i in s:
    if i!=term:
        result= result+i
        
print (result)