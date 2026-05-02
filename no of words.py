c=0
s= input('eneter a styering')
l=len(s)
for i in range(l):
    if s[i]== ' ':
        c=c+1
n=l-c
print(n)
