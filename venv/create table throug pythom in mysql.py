import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='naman123409',database='naman')
x=con.is_connected()
print(x)
cr=con.cursor()
s= '''create table students 
(name varchar(20) not null, 
 rollnumber int(3) primary key, 
 class int(2) not null, 
 sec varchar(2) check(sec in ('a','b','c','d','e','f','p')), 
 avg float(5,2))'''
cr.execute(s)
con.close()