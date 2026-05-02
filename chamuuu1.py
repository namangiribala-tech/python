l=[]
n=int(input('enter n'))
for i in range(n):
    x=int(input('enter a value'))
    l.append(x)
print(l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]%2!=0:
            if l[j]%2==0:
                l[i]=l[j]
            
print(l)
