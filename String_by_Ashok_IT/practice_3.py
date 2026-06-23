#3) Count vowels and consonants in string
string= input("Enter the String:- ")

vowel=0
consonants=0


for char in string:
    if char.isalpha():
        if char in "aeiou":
            vowel +=1
        else:
            consonants +=1


print("Vowels : ", vowel)
print("Consonants : ", consonants)