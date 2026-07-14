import sqlite3

# Establishing DB connection
connection = sqlite3.connect("student.db")

# Create cursor object to execute sql Queries
cursor= connection.cursor()

# We can using cursor to executing queries
cursor.execute("""
    create table if not exists students(
        student_id integer primary key autoincrement,
        student_name text,
        student_email text unique,
        student_course text,
        student_fee real
    )
""")

print("Student table created successfully............... ")

connection.commit()
connection.close()