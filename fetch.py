def reading():
    cursor.execute('SELECT * FROM company')
    data=cursor.fetchall()
    print(data)
