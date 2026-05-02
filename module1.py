def electbill():
    p=t/d
    q=[]
    print(p)
    for m in range(n):
        s=g[m]*p
        q.append(s)                                                       #a=present reading
    return q
t=float(input('enter the total electric bill'))
l=[]
e=[]
g=[]
n=int(input('no of floors'))
d=0
for i in range (n):
    print('enter present reading of',i,'floor')
    x=int(input())
    l.append(x)
for j in range (n):
    print('enter old reading of',j,'floor')
    y=int(input())
    e.append(y)
for k in range (n):
    f=l[k]-e[k]
    g.append(f)
    d+=f
z=electbill()
print(z)


