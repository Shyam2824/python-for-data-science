# Count occurence of each character in given string

string= input("Enter the String:- ")
char_count= {}

for char in string:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] =1
    
print("characteristic :- ")
for char, count in char_count.items():
    print(f" {char} : {count}") 