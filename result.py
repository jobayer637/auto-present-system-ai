import pymysql as database

con = database.connect(host='localhost', user='root',password='', database='face')
cursor = con.cursor()

val = cursor.execute('SELECT * FROM atd')
result = cursor.fetchall()

for rs in result:
    print rs

con.close()
