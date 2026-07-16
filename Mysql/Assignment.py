import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Shyam@2824"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")    # <-- Select the database

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks FLOAT
)
""")

conn.commit()

# -------------------- Add Student --------------------
def add_student():
    n = int(input("How many students do you want to add? "))

    for i in range(n):
        print(f"\nEnter Details of Student {i+1}")

        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        marks = float(input("Marks: "))

        sql = """
        INSERT INTO students(name, age, course, marks)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(sql, (name, age, course, marks))

    conn.commit()
    print(f"\n{n} Student(s) Added Successfully.")

# -------------------- View All Students --------------------
def view_all():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No Records Found.")
    else:
        print("\nID\tName\tAge\tCourse\tMarks")
        print("-"*50)
        for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")

# -------------------- View Student by ID --------------------
def view_by_id():
    sid = int(input("Enter Student ID: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Details")
        print("---------------")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Marks:", student[4])
    else:
        print("Student Not Found.")

# -------------------- Update Student --------------------
def update_student():
    sid = int(input("Enter Student ID to Update: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    if cursor.fetchone() is None:
        print("Student Not Found.")
        return

    name = input("New Name: ")
    age = int(input("New Age: "))
    course = input("New Course: ")
    marks = float(input("New Marks: "))

    sql = """
    UPDATE students
    SET name=%s, age=%s, course=%s, marks=%s
    WHERE id=%s
    """

    cursor.execute(sql, (name, age, course, marks, sid))
    conn.commit()

    print("Student Updated Successfully.")

# -------------------- Delete Student --------------------
def delete_student():
    sid = int(input("Enter Student ID to Delete: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    if cursor.fetchone() is None:
        print("Student Not Found.")
        return

    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()

    print("Student Deleted Successfully.")

# -------------------- Menu --------------------
while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all()

    elif choice == "3":
        view_by_id()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")

cursor.close()
conn.close()