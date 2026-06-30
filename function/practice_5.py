# fibonacci number 

def fib(n):
    if n <1:
        return None
    if n<3:
        return 1
    
    ele_1 = ele_2 = 1
    sum=0
    
    for i in range (3, n+1):
        sum= ele_1 +ele_2
        ele_1, ele_2 = ele_2, sum
        return sum
    
for n in range(1, 10):
    print(n, "==>", fib(n))