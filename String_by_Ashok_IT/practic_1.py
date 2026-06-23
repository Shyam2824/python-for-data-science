# reverse string
st1= input("Enter the string: ")

st2= reversed(st1)
print(st2)
print(list(st2))
print("".join(reversed(st1)))

st1= "ram"
st2=st1[::-1]
print (st2)