import sqlite3

# Establishing DB connection
connection = sqlite3.connect("student.db")

# Create cursor object to execute sql Queries
cursor= connection.cursor()


sql= "select * from students"

cursor.execute(sql)

students= cursor.fetchall()

print(type(students))

for student in students:
    print(student)