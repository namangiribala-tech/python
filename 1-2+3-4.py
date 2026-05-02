s=0
n= int(input('enter the vcalue of n'))
for i in range (1,n+1):
    if i%2 ==0:
            s= s+(i*-1)
    else:
        s= s+i
print (s)
