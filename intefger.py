a=int(input('enter the first digit'))
b=int(input('enter the second digit'))
if b>0 and b<9:
    c= (a+b)
elif b>9 and b<100:
    c= pow(a,2)
elif  b>=100 and b< 1000:
    c= pow(a,3)
else:
    c= pow(a,b)
print(c)
