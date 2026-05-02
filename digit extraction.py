ma= 0
mi= 9
a=int(input('enter a integer of four digit '))
while a!=0:
    rem= a%10
    if rem>ma:
        ma=rem
    elif rem<mi:
         mi=rem
    a=a//10
b= ma - mi
print(b)
