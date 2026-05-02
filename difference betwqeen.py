ma=0
mi=9
l=[]
n=int(input('enter the number of times'))
for i in range(n):
    x=int(input('enter a value'))
    l.append(x)
for i in range(n):
    if ma<l[i]:
        ma=l[i]
    else:
        if mi>l[i]:
            mi=l[i]
difference= ma-mi
print(difference)
        
