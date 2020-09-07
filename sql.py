import pymysql
import time
import datetime
from datetime import date, timedelta, datetime


# localtime = time.asctime( time.localtime(time.time()) )
# st = localtime.split(' ')
#
# print st
#
# tr = st[3]
# print tr.split(':')
#
#
# pDate = st[2]+'_'+st[1]+'_'+st[4]
# print(pDate)

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
#print current_time

now = datetime.now()
h = now.strftime("%H")
m = now.strftime("%M")
s = now.strftime("%S")

if int(h)>12:
    h=int(h)%12
else:
    h=h
tst = str(h)+':'+str(m)
print tst

if tst=='3:55':
    print 'loass your present'


# con = pymysql.connect(host='localhost', user='root',password='', database='face')
# cursor = con.cursor()
# Id=11
#
# cursor.execute('ALTER TABLE atd ADD '+pDate+' varchar(20)')
#
# # ?updateTable = 'UPDATE atd SET present="a" WHERE name="Jobayer"'
# cursor.execute('UPDATE atd SET present="p" WHERE id=%s',Id)
#
# con.commit()
# con.close()
