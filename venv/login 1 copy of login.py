import mysql.connector as m
user1 = input('Enter the username: ')
passwd1 = input('Enter the password: ')
data1 = input('Enter the database name: ')
host1 = 'localhost'
con = m.connect(host=host1, user=user1, passwd=passwd1, database=data1)
if con.is_connected()==True:
     print('Successfully connected to the database')
     cr=con.cursor()

def login():
    username = input("Enter username: ") 
    password = input("Enter password: ")
    query = "SELECT username,password,role FROM worker WHERE username = '{}'".format(username)
    cr.execute(query)
    result = cr.fetchone()
    if result[1]==password:
            a='succesfull'
            return result ,a 
    else:
         return exit('wrong credentials')
def addcar():
      ch='y'
      while ch=='y':
       cuid=int(input('enter the cid of car'))
       b=input('enter the brand name of the car')
       m=input('enter the car model')
       rno=input('enter the registrationnumber of the car')
       sc= int(input('enter the seating capacity of the vechile'))
       ppd=float(input('enter the price per day of renting the car'))
       s='''insert into car(car_id,brand,model,registrationno,seatingcapacity,priceperday)
               values({},'{}','{}','{}',{},{},)'''.format(cuid,b,m,rno,sc,ppd)
       cr.execute(s)
       con.commit()
       print('car added succesfully')
       ch=input('do you want to continue adding more cars y or n')

def removecar():
      print('removing car but before that search the car which u want to remove by')
      print('1. by car id')
      print('2. by car brand')
      print('3. by registration number')
      c=input('enter number by which method')
      if c=='1':
            ch='y'
            print('you are removing car by car id')
            while ch=='y':
             ci=int(input('enter the car id'))
             print('ok loading..... before removing the car check the details of the car ')
             s= 'select * from car where carid={}'.format(ci)
             cr.execute(s)
             de=cr.fetchall()
             for i in de:
                   for j in i:
                         print(j,end='\t')
                   print()
             print('check all the details carefully')
             cia=int(input('again enter the car id'))
             print( 'removing the details')
             s='remove from car where carid={}'.format(cia)
             cr.execute(s)
             con.commit()
             print('car removed from database succesfully')
             ch=input('do you wantto continue removing more cars by car id method y or n')
      elif c=='2':
            ch='y'
            print('you are removing car by brand method')
            while ch=='y':
                  cb=input('enter the car brand')
                  print('ok loading..... before removing the car check the details of the car ')
                  s= "select * from car where brand='{}'".format(cb)
                  cr.execute(s)
                  db=cr.fetchall()
                  for i in db:
                       for j in i:
                            print(j,end='\t')
                  print()
                  print('check all the details carefully')
                  cia= int(input('enterthe cid you wantto remove'))
                  print( 'removing the details')
                  s="remove from car where car_id='{}'".format(cia)
                  cr.execute(s)
                  con.commit()
                  print('car removed from database succesfully')
                  ch=input('do you want to continue removing more cars by car brand method y or n')
      elif ch=='3':
            ch='y'
            while ch=='y':
             cm=input('wenter your registration number')  
             print('ok loading..... before removing the car check the details of the car ')   
             s= "select * from car where registrationno='{}'".format(cm)
             cr.execute(s)
             df=cr.fetchall()
             for i in db:
                       for j in i:
                            print(j,end='\t')
             print()
             print('check all the details carefully')
             crn= int(input('enter the cid you want to remove'))
             print( 'removing the details')
             s="remove from car where car_id='{}'".format(crn)
             cr.execute(s)
             con.commit()
             print('car removed from database succesfully')
             ch=input('do you want to continue removing more cars by car registration number method y or n')

def viewcar():
     print('1.search by particual brand')
     print('2. see all cars')
     co=input('you want to view cars by')
     if co=='1':
          print('you want to search by brand name')
          b=input('enter the brand name')
          s="select * from car where brand='{}'".format(b)
          cr.execute(s)
          data= cr.fetchall()
          for i in data:
               for j in i:
                    print(j,end='\t')
          print()
     elif co=='2':
        s='select * from car '
        cr.execute(s)
        data=cr.fetchall()
        for i in data:
            for j in i:
                  print(j,end='\t')
        print()

def addemployee():
      print('you want to add employee')
      ch='y'
      while ch=='y':
            name=input('enter the name of the employee')
            phoneno=int(input('enter the number of the employee'))
            emailid=input('enter the email id of the employee')
            u=input('enter the usrername of the employee')
            p=input(' enter the password of the employee')
            role=input('enter the roll of the employee')
            salary=int(input('enter the salary of the employee'))
            s='''insert into worker(name,phoneno,emailid,username,password,role,salary)
                  values ('{}',{},'{}','{}','{}','{}',{})'''.format(name,phoneno,emailid,u,p,role,salary)
            cr.execute(s)
            con.commit()
            ch=input('do you want to continue y/n')

def viewemp():
      s='select * from worker '
      cr.execute(s)
      data2=cr.fetchall()
      for i in data2:
            for j in i:
                  print(j,end='\t')
      print()

def updateemp():
      print('you have selected to update the information of existing employee')
      gg='y'
      while gg=='y':
       print('check the employee details ')
       print('1.name')
       print('2.employee id')
       c=input('enter the no')
       if c=='1':
             e=input('enter the name of the employee')
             s="select * from worker where name='{}'".format(e)
             cr.execute(s)
             d=cr.fetchall()
             for i in d:
                   for j in i:
                         print(j,end='\t')
             print()
       elif c=='2':
             e=input('enter the id of the employee')
             s="select * from worker where worker_id='{}'".format(e)
             cr.execute(s)
             d=cr.fetchall()
             for i in d:
                   for j in i:
                         print(j,end='\t')
             print()
       print('check the details carefully')
       iid=int(input('enter the id of the employee you want to update of'))
       print ('what do you want to update of the employee')
       print('1. email id')
       print('2. phone no')
       print('3. username')
       print('4. password')
       print('5. salary')
       print('one at each time')
       up=input('enter the number')
       if up =='1':
             print('you want to update the email of the employee')
             u=input('enter the email id of the employee')
             sc="update worker set emailid='{}' where worker_id={}".format(u,iid)
             cr.execute(sc)
             con.commit()
       elif up=='2':
             print('you want to update the phone no of the employee')
             u=input('enter the new phone no of the employee')
             sc="update worker set phone_no ={} where worker_id={}".format(u,iid)
             cr.execute(sc)
             con.commit()
       elif up=='3':
             print('you want to update the  of the employee')
             u=input('enter the email id of the employee')
             sc="update worker set emailid='{}' where worker_id={}".format(u,iid)
             cr.execute(sc)
             con.commit()
       elif up=='4':
             print('you want to update the password')
             u=input('enter the paswword of the employee')
             sc="update worker set password='{}' where worker_id={}".format(u,iid)
             cr.execute(sc)
             con.commit()
       elif up=='5':
             print('you want to update the salary')
             u=int(input('enter the salary of the employee'))
             sc="update worker set salary={} where worker_id={}".format(u,iid)
             cr.execute(sc)
             con.commit()
      gg=input('do you ewant to update more datas')

def deleteemp():
      print('you have selected to delete the information of existing employee')
      gy='y'
      while gy=='y':
       print('check the employee details ')
       print('1.name')
       print('2.employee id')
       c=input('enter the no')
       if c=='1':
             e=input('enter the name of the employee')
             s="select * from worker where name='{}'".format(e)
             cr.execute(s)
             d=cr.fetchall()
             for i in d:
                   for j in i:
                         print(j,end='\t')
             print()
       elif c=='2':
             e=input('enter the id of the employee')
             s="select * from worker where worker_id='{}'".format(e)
             cr.execute(s)
             d=cr.fetchall()
             for i in d:
                   for j in i:
                         print(j,end='\t')
             print()
       print('check the details carefully')
       iid=int(input('enter the id of the employee you want to delete of'))
       s='remove from worker where worker_id={}'.format(iid)
       cr.execute(s)
       con.commit()

def employeemenu1():
      print('..........welcome to the car rental manager system.........')
      print('1.rent a car')
      print('2. return a car')
      print('3.view all cars')
      print('4.add a customer')
      print('5.view all cars')
      print('6.exit')
      go=input('enter the number for work')
      if go=='1':
            print('you chiose to rent a car option')
            

      








      






      
      


      



def employeemenu():
      ch='y'
      while ch=='y':
        print("--- welcome to Employee Management Menu ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee Information")
        print("4. Delete Employee")
        print("5. Exit to Main Menu")
        c=input('enter your choice')
        if c=='1':
            addemployee()
        elif c=='2':
            viewemp()
        elif c=='3': 
            updateemp()
        elif c=='4':
            deleteemp()
        elif c=='5':
            break

def carmenu():
      ch='y'
      while ch=='y':
        print('1. add car')
        print('2. remove car')
        print('3. view car')
        print('4. logout')
        c=input('enter your choice')
        if c=='1':
              addcar()
        elif c=='2':
              removecar()
        elif c=='3':
              viewcar()
        elif c=='4':
              break
        ch=input('do you want to continue y/n')





def managermenu():
      print('...welcome manager of the store....')
      ch='y'
      while ch=='y':
            print('1. car menu')
            print('2. employee menu')
            print('3. sales menu')
            print('4. logout')
            c=input('which menu you want to see')            
            if c=='1':
                  carmenu()
            elif c=='2':
                  employeemenu()
            elif c==3:
                  salesmenu()
            elif c==4:
                  exit()
      ch=input('do you want to continue y/n ')

      






d=login()
print(d[1])
if d[0][2]=='manager':
      managermenu()
else:
      employeemenu1()

    