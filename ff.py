l=[]
n=int(input('no of times'))
for i in range(0,n):
    x=eval(input('enter value'))
    l.append(x)
for i in range(0,len(l)):
    if type(l[i])==int :
        l[i]%2==0
        l[i]+1
    elif l[i]%2==1:
        l[i]-1
    else:
        pass
print(l)