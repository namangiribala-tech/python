n= int(input('no of times'))
c=0
lstr=""
i=1
while i<=n:
    s=input('enter a string')
    l= len(s)
    if l>c:
        c=l
        string= s
    i=i+1
print(string)
    
