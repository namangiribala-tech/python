import mysql.connector as m
user1 = input('Enter the username: ')
passwd1 = input('Enter the password: ')
data1 = input('Enter the database name: ')
host1 = 'localhost'
con = m.connect(host=host1, user=user1, passwd=passwd1, database=data1)
if con.is_connected()==True:
     print('Successfully connected to the database')
     cr=con.cursor()
s='select * from worker'
cr.execute(s)
data=cr.fetchall()
if data==[]:
     name=input('enter the name of the employee')
     phoneno=int(input('enter the phone number of the employee'))
     emailid=input('enter the email id of the employee')
     u=input('enter the usrername of the employee')
     p=input(' enter the password of the employee')
     role=input('enter the roll of the employee')
     salary=int(input('enter the salary of the employee'))
     s='''insert into worker(name,phone_no,emailid,username,password,role,salary)
             values ('{}',{},'{}','{}','{}','{}',{})'''.format(name,phoneno,emailid,u,p,role,salary)
     cr.execute(s)
     con.commit()
else: print('there is a employee')