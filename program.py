n=int(input('no of times'))
e={}
for i in range(n):
    name=input()
    marks=input()
    e[name]=[marks]
for i in e :
    if i[0] == 'a':
        if e[i]['marks']>=40:
            print(i)
        