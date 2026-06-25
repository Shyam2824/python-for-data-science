#remove vowels

user_word = input("")
user_word = user_word.upper()

for letter in user_word:
    if letter in 'AEIOU':
        continue
    print(letter)