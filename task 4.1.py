import electricbillcalculator12_module as e

#---- bill calcilationn for user a----
a=int(input("enter the number of consumption units for user a "))
d=e.electricc(a)
print("total amount charged",d)

#----bill calculation for user b----
b=int(input("enter the number of consumption units for user b "))
f=e.electricc(b)
print("total amount charged",f)


#----comparison-----
print("User A: Units =", a, "Bill = Rs.", d)
print("User B: Units =", b, "Bill = Rs.", f)
if a>b:
    di=int(((a-b)/b)*100)
    print("user a consumed ",di,"% more than the user b")
    print("user a paid",d-f," rupees more than the user b")
elif b>a:
    di=int(((b-a)/a)*100)
    print("user b consumed ",di,"% more than the user a")
    print("user b paid",f-d," rupees more than the user a")
else:
    print("both the users have paid equal amount of money ")
