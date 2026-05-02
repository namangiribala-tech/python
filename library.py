lib={}
while true:
    print('enter your choice(1=add,2=update or 3=exit)')
    ch=int(input('enter your numerical choice'))
    if ch==1:
        n=int(input('enter no of times'))
        for i in range(n):
            title=input('enter title of thge book')
            author=input('enter the author name ')
            pub=input('enter the publisher namer')
            if title not in lib:
            lib[title]={'authr':author,'publisher':pub}
        print(lib)
    elif ch==2:
        auth=input('enter a author name')
        for i in lib:
            if lib[i]['authr']==auth:
                newpubli=input('enter he new publisher name')
                lib[i]['publisher']=newpubli
    elif ch==3:
        
                
            
        
    
