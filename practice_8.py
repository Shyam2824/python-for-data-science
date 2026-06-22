# if year is leap or common

years= int(input("Enter the years:- "))

if years%4 !=0:
    print(" Common year ", years)
elif years%100 !=0:
    print(" Common year ", years)
elif years%400 !=0:
    print(" Common year ", years)
else:
    print("this is Leap year", years)