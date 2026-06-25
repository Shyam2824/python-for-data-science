# Remove Duplicate Characters in String

string= input("Enter the String : - ")

result =""

for char in string:
    if char not in result:
        result += char
        
print("String after removing duplicates: ", result)


string2= input("Enter the string:= ")
result="".join(set(string))
print(result)