gen= input('enter your gender')
ser= int(input('enter your service period'))
salary= float(input('enter your salary'))
if gen=="m":
    if salary>= 30000 and ser>10 :
        i= 'insured'
    elif salary< 30000 and ser>15:
        i= 'insured'
    else:
        i= 'not insured'
elif gen== 'f':
    if salary>= 20000 and ser>7:
        i= 'insured'
    elif salary < 20000 and ser >10:
        ii= 'insured'
    else:
        i= 'not insured'
print(i)
        
        
