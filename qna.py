n= int(input())
x= int(input())
s = 1
for i in range (2,n+1):
    s= s+1/(x**i)
print(s)
