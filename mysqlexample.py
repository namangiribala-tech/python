import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='naman123409',database='naman')
x=con.is_connected()
print(x)
