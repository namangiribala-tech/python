n= int(input(''))
for i in range(1,n):
    c=0
for j in range (1,n):
    if i%j ==0:
        c=c+1
    if c == n:
        print('perfect')
