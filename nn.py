n= input('enetr a syring')
s=c=0
m=len(n)
b='1234567890'
for i in range(m):
    if n[i] in b:
        c=c+1
        s=s+int(n[i])
d=s/c
print('avg of digits',d)
        
    
    
