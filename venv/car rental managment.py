import mysql.connector as m
user1 = input('Enter the username: ')
passwd1 = input('Enter the password: ')
data1 = input('Enter the database name: ')
host1 = 'localhost'
con = m.connect(host=host1, user=user1, passwd=passwd1, database=data1)
if con.is_connected()==True:
     print('Successfully connected to the database')
     cr=con.cursor()
print('.........WELCOME TO CAR RENTAL MANAGMENT SYSTEM.........')

def newcustomer():
     # to add new customer 
     cid= int(input('enter your customer id'))
     name=input('enter your name')
     phno=int(input('enter your phone number'))
     address=input('enter your address')
     prefix=input('enter the prefix of your driving licence')
     dlno=int(input('enter your licence no'))
     s="insert into customer(customerid,name,phno,address,prefix,drivinglicenseno)values({},'{}',{},'{}','{}',{})".format(cid,name,phno,address,prefix,dlno)
     cr.execute(s)
     con.commit()

def existing():
     chose=input('you want to search by 1 for cid or 2 for name')
     if chose=='1':
          cid=int(input('enter your cid'))
          s="select * from customer where customerid={}".format(cid)
          cr.execute(s)
     elif chose=='2':
          name1=input('enter your name')
          s="select * from customer where name='{}'".format(name1)
          cr.execute(s)
     data=cr.fetchall()
     print(data)

     
     
     



customer = input('are you a new customer  y/n')
if customer=='y':
     newcustomer()
elif customer=='n':
     existing()

