n= int (input('enter the value of n'))
for i in range(n):
    name= input('enter the name of students')
    phy= float(input('enter the marks of phy'))
    chem= float(input('enter the marks of chem'))
    math= float(input('enter the marks of math'))
    avg=(math+chem+phy)/3
    if avg>=90:
        gr='A'
    elif avg>=70:
        gr='b'
    elif avg>=50:
        gr='c'
    else:
        gr= 'f'
    print('avg=', avg)
    print('grade =',gr)
    
