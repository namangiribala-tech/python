def electricc(a):
    if a<=100:
        print("as your consumption is less")
        print("your are charged 0 rupees")
    elif a>100 and a<=200:
        print ("as you have consumed more than 100 units so we will charge 5 rupees")
        b=(a-100)*5
        c=0
        print("total amount charged is ",b)
        return b+c
    elif a>200:
        print("as your consuption is more than 200 so more than 200 we charge 10")
        b=100*5
        if a-200!=0:
            c=(a-200)*10
        else:
            c=0
    
        print(f"""                  you have been charged for first 100 units is                               0 
                  for next 100 units that is 5 rupees that will be                          {b} 
                  and later on for more than 200 we have charged you 10 rupees that will be {c}
                  ---------------------------------------------------------------------------------------- 
                  and total becomes                                                         {b+c} """)
        return b+c
