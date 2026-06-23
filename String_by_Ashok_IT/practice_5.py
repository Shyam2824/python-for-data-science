# Remove Duplicate Characters in String

string= input("Enter the String : - ")

result =""

for char in string:
    if char not in result:
        result += char
        
print("String after removing duplicates: ", result)