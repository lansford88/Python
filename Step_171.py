import sqlite3
import os

conn_171 = sqlite3.connect('Step_171.db')

with conn_171:
    curs = conn_171.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS tbl_mainFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn_171.commit()
conn_171.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.png', 'World.txt', 'data.pdf', 'myPhoto.jpg')


conn_171 = sqlite3.connect('Step_171.db')

with conn_171:
    curs = conn_171.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            curs.execute("INSERT INTO tbl_mainFiles(col_filename) VALUES (?)",\
                (file,))
            conn_171.commit()
conn_171.close()

conn_171 = sqlite3.connect('Step_171.db')

with conn_171:
    curs = conn_171.cursor()
    curs.execute("SELECT * FROM tbl_mainFiles")
    results = curs.fetchall()
    print(results)

conn_171.close()
             
