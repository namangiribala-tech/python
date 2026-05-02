'''this is my module'''
def electbill():
    '''this fun is used to calculate the electric bill of the fun sub reading wise'''
    p=t/d
    q=[]
    print(p)
    for m in range(n):
        s=g[m]*p
        q.append(s)                                                       
    return q
t=float(input('enter the totalelectric bill'))
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
def salary(bs):
    '''calculate the salary of a person with ds and ra'''
    ra=0.8*bs
    ds=0.35*bs
    total=bs+ra+ds
    print(total)
print('welcome to my program')
x=int(input('enter your basic salary'))
salary(x)
