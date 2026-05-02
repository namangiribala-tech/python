n=int(input())
a=[]
b=[]
c=[]
d=[]
e=[]
for i in range(n):
    x=int(input('entewr value'))
    y=int(input('entewr value'))
    a.append(x)
    b.append(y)
for i in range (n):
    if a[i]%2==0:
        c.append(a[i])
    else:
        d.append(b[i])
for i in range (n):
    if b[i]%2==0:
        c.append(b[i])
    else:
        d.append(b[i])
e=d[::-1]
print(c+e)
