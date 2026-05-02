import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='naman123409',database='naman')
x=con.is_connected()
print(x)
cr=con.cursor()
def add():
    ch='y'
    while ch=='y':
        id=input('enter the id of product')
        name=input('enter the namem of thej peoduct')
        price=float(input('enter the price of the product'))
        qty=int(input('enter the quantityof product'))
        category=input('enter the category or give null')
        cr.execute("insert into product values['{}','{}',{},{},'{}']").format(id,name,price,qty,category)
        con.commit()
        input('do you want to continue y or n')
add()