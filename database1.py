import sqlite3
import time
import random
from datetime import date
from datetime import datetime

connection=sqlite3.connect('company2.db') #to create database
cursor=connection.cursor() #to save changes

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS company(name TEXT,surname TEXT,number REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS datetime(tvalue TEXT,date TEXT,lang TEXT,value TEXT)')

def data_entries():
    cursor.execute("INSERT INTO company VALUES('Parth','Doshi',15)")
    cursor.execute("INSERT INTO company VALUES('Rockstar','Boy',16)")
    cursor.execute("INSERT INTO company VALUES('Fun','Champ',17)")
    connection.commit()
def reading():
    cursor.execute('SELECT * FROM company')
    data=cursor.fetchall()
    print(data)
def dynamic_entry():
    tvalue=time.time()
    date=str(datetime.fromtimestamp(tvalue).strftime('%Y-%m-%d %H:%M:%S'))
    lang='Python'
    value=random.randrange(0,10)
    cursor.execute("INSERT INTO datetime(tvalue,date,lang,value) VALUES(?,?,?,?)",(tvalue,date,lang,value))
    connection.commit()

create_table()
data_entries()
reading()
dynamic_entry()


