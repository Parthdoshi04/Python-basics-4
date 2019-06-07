import sqlite3

connection=sqlite3.connect('student.db')
cursor=connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS studentdetails(name TEXT,rollno NUMBER,sapid NUMBER,course TEXT,year NUMBER,gender TEXT)')
def dynamic_entry():
    name=input("Enter name: ")
    rollno=int(input("Enter roll number: "))
    sapid=int(input("Enter sap id: "))
    course=input("Enter the course name & branch: ")
    year=int(input("Enter the current year: "))
    gender=input("Enter the gender: ")
    cursor.execute("INSERT INTO studentdetails(name,rollno,sapid,course,year,gender) VALUES(?,?,?,?,?,?)",(name,rollno,sapid,course,year,gender))
    connection.commit()
def read():
    cursor.execute('SELECT * FROM studentdetails WHERE gender="Female"')
    data=cursor.fetchall()
    print(data)
create_table()
dynamic_entry()
read()
