n=int(input())
e={}
for i in range(n):
    name=input()
    ds=input()
    sal=float(input())
    sp=float(input())
    e[name]={'designation':ds,'salary':sal,'service period':sp}
for i in e:
    if e[i][designation]=='clerk'and e[i]['service period']>=10:
        s=s+e[i][salary]
        c=c+1
avg=s/c
print('avg salary',avg)
         
