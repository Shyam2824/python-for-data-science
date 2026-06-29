# Create Account

print("===== CREATE ACCOUNT =====")
saved_username = input("Create Username : ")
saved_password = input("Create Password : ")

print("\nAccount Created Successfully!\n")

# Login

print("===== LOGIN =====")
username = input("Enter Username : ")
password = input("Enter Password : ")

if username == saved_username and password == saved_password:
    print("\nLogin Successful!")
    print("Welcome,", username)
else:
    print("\nInvalid Username or Password.")