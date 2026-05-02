n=int(input('enter a value '))
l=[]
for i in range(n):
    x=input('enter a value of element')
    l.append(x)
m=0
for i in range(n):
    if m < len(l[i]):
        m=len(l[i])
        p=i+1
        y=l[i]
print('position',p)
print('no of charecter',y)

    
