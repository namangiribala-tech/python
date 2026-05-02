print("bill analytics system")
a=int(input("enter your units consumed"))
if a<0:
    print("invalid input")
    exit()
else:
    print("tier1= 0 - 100")
    print("tier2= 100 - 200 charged rs.5 per unit ")
    print("tier3= 200 - unit charged rs.10 per unit ")
    print("-----billing breakdown-----")
    if a>100 and a<200:
         c=(a-100)
         d=c*5
         print("for first 100 units you will be charged 0 rupees                         ","\t","100 x 0 ","0")
         print("for next that is tier2 per units you will be charged 5 rupees              ","\t",c," x 5 ",d)
         print("----------------------------------------------------------------------------------------------")
         print("you will be charged                                                                      ",d)
    
    elif a-200!=0:
        b=100*5
        c=(a-200)
        d=c*10
        print("for first 100 units you will be charged 0 rupees                                      ","\t","100 x 0=","0")
        print("for next that is tier2 per units you will be charged 5 rupees                        ","\t","100 x 5=",b)
        print("for next more than 200 that is tier3 per units you will be charged 10 rupees remaining ","",c,"x 10=",d)
        print("--------------------------------------------------------------------------------------------------------")
        print("total you will be charged                                                                         ",b+d)

if 0<a<150:
    print("economical use low consuption")
elif 151<a<250:
    print("average use moderate user")
elif a>250:
    print("high use energu efficrncy alert")
