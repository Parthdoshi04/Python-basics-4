import sqlite3
connection=sqlite3.connect('company.db') #to create database
cursor=connection.cursor() #to save changes

cursor.execute("SELECT * FROM company WHERE surname='Doshi'")
print(cursor.fetchall())
connection.commit()
