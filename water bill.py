def waterbill():
    p=int(input('enter the present water reading'))
    o=int(input('enter the previous water reading'))
    q=p-o
    n=int(input('enter the no of floors'))
    l=[]
    for i in  range(n):
        print('enter the no of members',i,'floor')
        m=int(input())
        x=+m
        l.append(m)
    r=q/x
    for i in range(len(l)):
        x=l[i]*r
        l[i]=x
    return l
z= waterbill()
print(z)

    

