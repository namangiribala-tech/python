bank={}
print('enter numeric value 1-add, 2-withdraw,3- deposit, 4-delete')
ch=int(input('enter your choice'))
if ch==1:
    n=int(input('enter your no of datas you want to move'))
    c=0
    while c!=n:
        accno= int(input('enter your accno'))
        if accno not in bank:
            name=input('enter your name')
            bal=int(input('enter your balance'))
            bank[accno]={'name':name,'balance':bal}
            c=c+1
            print(bank)
        else:
            print('already available')
elif ch==2:
    accno=int(input('enter your account no'))
    if accno in bank:
        print(bank[accno])
        wa=int(input('enter amount you want to withdraw'))
        if bank[accno]['balance']-wa>1000:
            print('succesfull withdraw')
            bank[accno]['balance']-=wa
        else:
            print('insufficient balance')
    else:
        print('account no not available')
elif ch==3:
    accno=int(input('enter the account number'))
    if accno in bank:
        bal=int(input('enter the amount want to deposit'))
        bank[accno]['balance']+=bal
        print('deposit succesfull')
    else:
        print('account no not available')
elif ch==4:
    name=input('enter your name')
    accno=int(input('enter your account number'))
    if bank[accno]==accno and bank[accno]['name']==name:
        del(bank[accno])
        print('your account was succesfully deleted from bank')
        print(bank)