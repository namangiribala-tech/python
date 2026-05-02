x= int(input('enter thre valuer of x'))
n= int(input('enter thre valuer of n'))
s=0
for i in range (1,n+1):
   if i == 2:
       s=s-pow(x,i)
   else:
       s= s+pow(x,i)
print(s)
    
