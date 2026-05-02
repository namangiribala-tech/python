import mysql.connector as m
user1=input('enter the username')
passwd1=input('enter the password')
data1=input('enter database name')
host1='localhost'
con=m.connect(host=host1,user=user1,passwd=passwd1,database=data1)
if con.is_connected()==True:
    print('succesfull')
else:
    print('failed')
cr=con.cursor()
def add():
    ch='y'
    while ch=='y':

        id=input('enter the id of product')
        name=eval(input('enter the namem of thej peoduct'))
        price=float(input('enter the price of the product'))
        qty=int(input('enter the quantityof product'))
        category=input('enter the category or give null')
        s="insert into product values['{}','{}',{},{},'{}']".format(id,name,price,qty,category)
        cr.execute(s)
        con.commit()
        input('do you want to continue y or n')
print('welcome to inventory managment')
print('''choose from the option below
      1. add new product
      2. update product
      3. remove product
      4. product query
      5. category managment ''')
choice=int(input('enter yout choice...'))
if choice==1:
    add()

    