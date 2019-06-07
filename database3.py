def dynamic_entry():
    tvalue=time.time()
    date=str(datetime.datetime.fromtimestamp(tvalue).strftime('%Y-%m-%d %H:%M:%S'))
    lang='Python'
    value=random.range(0,10)
    cursor.execute("INSERT INTO company(tvalue,datestamp,lang,value) VALUES(?,?,?,?)",(tvalue,datestamp,lang,value))
    connection.commit()
