e={}
n=int(input())
for i in range(n):
    name=input()
    marks= int(input())
    e[name]={'mk':marks}
for i in e :
    if i[0]=='a'and e[i]['mk']>=40:
        print(i)
