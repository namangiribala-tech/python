#-----seasonl chmge & peak hour consumption ---------
"""s=input("enter your season: summer, winter,raining").lower()
a=int(input("enter your units consumption"))
if s=="summer":
    y=input("do you have ac").lower()
    print("as t is summer the prices are increased")
    if y=="yes":
        m=a*0.2
        d=a*0.5
        n=a*0.3
        print("---------------------------------------------------------------")
        print("phase of day"," ","% considered"," ", "total units"," ","rate"," ","total amount")
        print("  morning ","\t","20 %","\t\t", m,"\t   ",3,"\t   ",m*3)
        print("  afternoon ","\t","50 %","\t\t", d,"\t   ",12,"\t   ",d*12)
        print("  night ","\t","30 %","\t\t", n,"\t   ",7,"\t   ",n*7)
        print("---------------------------------------------------------------")
        print("total                                                   ", m*3 +d*12+n*7)
    else:
        m=a*0.25
        d=a*0.45
        n=a*0.3
        print("---------------------------------------------------------------")
        print("phase of day"," ","% considered"," ", "total units"," ","rate"," ","total amount")
        print("  morning ","\t","20 %","\t\t", m,"\t   ",3,"\t   ",m*2)
        print("  afternoon ","\t","50 %","\t\t", d,"\t   ",12,"\t   ",d*12)
        print("  night ","\t","30 %","\t\t", n,"\t   ",7,"\t   ",n*7)
        print("---------------------------------------------------------------")
        print("total                                                   ", m*3 +d*12+n*7)
elif s=="raining":
    m=a*0.3
    d=a*0.25
    n=a*0.45
    print("---------------------------------------------------------------")
    print("phase of day"," ","% considered"," ", "total units"," ","rate"," ","total amount")
    print("  morning ","\t","30 %","\t\t", m,"\t   ",2,"\t   ",m*2)
    print("  afternoon ","\t","25 %","\t\t", d,"\t   ",11,"\t   ",d*11)
    print("  night ","\t","45 %","\t\t", n,"\t   ",6,"\t   ",n*6)
    print("---------------------------------------------------------------")
    print("total                                                   ", m*2 +d*11+n*6)
elif s=="winter":
    m=a*0.4
    d=a*0.2
    n=a*0.4
    print("---------------------------------------------------------------")
    print("phase of day"," ","% considered"," ", "total units"," ","rate"," ","total amount")
    print("  morning ","\t","40 %","\t\t", m,"\t   ",5,"\t   ",m*5)
    print("  afternoon ","\t","20 %","\t\t", d,"\t   ",4,"\t   ",d*4)
    print("  night ","\t","40 %","\t\t", n,"\t   ",5,"\t   ",n*5)
    print("---------------------------------------------------------------")
    print("total                                                   ", m*5 +d*4+n*5)"""

#-------- PREDICTIB=VE BILL ALEERT---------

"""a=input("enter the next months seqson going to be like summer winter raining").lower()
b=int(input("previoud months units"))
c=int(input("enter this month units"))
if a=="summer":
    y=input("do you have ac").lower()
    if y=="yes":
        d=((c-b)/b)*100
        d=+10
        print(f"your bill is going to increase by {d} % in next month")
    elif y=="no":
         d=((c-b)/b)*100
         d+=5
         print(f"yout bill is going to increase by {d} % in next month")
elif a=="raining":
    d=((c-b)/b)*100
    d=+5
    print(f"your bill is going to increase by {d} % in next month")
elif a=="winter":
    d=((c-b)/b)*100
    d=+2
    print(f"your bill is going to increase by {d} % in next month")"""

#------ energy saving tips-------
units = float(input("Enter total electricity units consumed: "))

print("\n--- Energy Saving Recommendations ---")

if units <= 150:
    print("✅ Low consumption! Keep it up.")
    print("💡 Tip: Continue using LED bulbs and energy-efficient fans.")
elif units <= 300:
    print("⚠️ Moderate consumption detected.")
    print("💡 Tip: Turn off lights and fans when not in use.")
    print("💡 Tip: Use washing machines and geysers during off-peak hours.")
else:
    print("🚨 High consumption! Consider reducing usage.")
    print("💡 Tip: Use energy-efficient appliances (5-star rated).")
    print("💡 Tip: Set your AC temperature to 25°C or higher.")
    print("💡 Tip: Unplug devices when not in use to avoid standby power loss.")

print("\nThank you for using the Energy Saver Assistant ⚡")


    

    
