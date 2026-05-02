import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='naman123409',database='naman')
x=con.is_connected()
print(x)
cr=con.cursor()
y='y'
while y=='y':
    a=int(input('enter rollno'))
    b=input('enter name')
    c=int(input('enter class'))
    d=input('enter sec')
    s= '''insert into students(rollnumber , name , class, sec) 
    values({},'{}',{},'{}')'''.format(a,b,c,d)
    cr.execute(s)
    con.commit()
    y=(input('enter do you want to continue'))
con.close()