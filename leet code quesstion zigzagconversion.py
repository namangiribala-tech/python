def zigzag(a,b):
    d=1
    c=3#( it will repeat f 3 times inloop for 3 times print )
    l=[]
    m=0
    for i in range(b+b):
        if d%2==0:
            x=[" ",a(m+1)," "]
            l.append(x)
            d+=1
            m+=1
        else:
            x=[]
            for i in range(1,c+1):
                x.append(a(m+i))

            l.append(x)    
            m+=3
            d+=1
    else:
        n,m,k=[],[],[]
        for i in l:
            for j in i:
                if j==0:
                    m.append(j)
                elif j==1:
                    n.append(j)
                elif j==2:
                    k.append(j) 
        print(m)
        print(n)
        print(l)
a=input("enter your sentense")
n=int(input("entr your dydte"))
zigzac////////////////////////////////////////////////////
