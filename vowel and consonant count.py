s=c=0
v="AEIOUaeiou"
a= input('eenter a string ')
q=len(a)
for i in a:
    if i in v:
            s=s+1
    else:
        c=c+1
print('no of vowels=', s)
print('no of consonants', c)
        
