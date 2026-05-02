n= int(input('enter the no of rep[eatition'))
s=0
l=[]
c=0
for i in range(n):
    x=int(input('enter a value'))
    l.append(x)
for i in range(len(l)):
    if l[i]%2==1:
        c=c+1
        s=s+l[i]
avg= s/c
print(avg)
