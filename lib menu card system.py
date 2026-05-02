lib={}
blist={}
print('which option would like yto choose 1=add,2=update,3=exit')
ch=int(input('choose the numerocal value'))
n=int(input('enter no of values'))
while True:
    if ch==1:
        for i in range (n):
            title=input('enter thr title of thr book')
            author=input('enter the name of author')
            publisher=input('enter the publisher name')
            if title not in lib:
                lib[title]={'name of author':author,'name of publisher':publisher}
        print(lib)
        break
    elif ch==2:
        authorname=input('enter the new author name')
        newpub=input('enter the new publisher name')
        if lib[title][author]==authorname:
            lib[title][publisher]=newpub
    elif ch==3:
        break

