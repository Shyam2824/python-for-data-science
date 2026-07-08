# get number of input

class Bank:
    def __init__(self, account, branch, amount):
        self.account= account
        self.branch= branch
        self.amount=amount
        
    def display(self):
        print("=======================")
        print("Account no. ", self.account)
        print("Branch ", self.branch)
        print("Amount  ", self.amount)
        
n= int(input("Enter the no of customer: "))
customer=[]

for i in range(n):
    print(f" Customer : {i+1}")
    
    account= int(input("Enter your account number: "))
    branch= input("Enter your branch name: ")
    amount= input("Enter your amount number: ")
    
    c1= Bank(account, branch, amount)
    customer.append(c1)
    print("\n Account details")
for j in customer:
    j.display()