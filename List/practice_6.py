# find the greatest  number in the list
lst = [15, 57, 44, 10, 85, 99, 25 ]   
 
largest=lst[0]

for i in range(1,len(lst)):
    if lst[i]>largest:
        largest = lst[i]

print(largest)

n = int(input())
lst = [int(input()) for _ in range(n)]
print(lst)