def abc(x):
    for i in range(1,x):
        if x%8==0:
            return'good'
        print(i)
    else:
        return'bye'
n=int(input('enter no'))
z=abc(n)
print(z)