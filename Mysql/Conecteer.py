import sqlite3

# Establishing DB connection
connection = sqlite3.connect("student.db")

# Create cursor object to execute sql Queries
cursor= connection.cursor()

# Read student information
student_name= input("Enter the Student name: ")
student_email= input("Enter the Student email: ")
student_course= input("Enter the Student course: ")
student_fee= input("Enter the Student fee: ")

sql = "insert into students (student_name, student_email, student_course, student_fee) values(?, ? , ?, ?)"

cursor.execute(sql,(student_name, student_email, student_course, student_fee))

connection.commit()

print("Student insert Successfully......")

connection.close()


