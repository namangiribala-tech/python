def percentage(students):
    for i  in students:
        total=sum(i["marks"])
        percentage=(total/300)*100
        i["percentage"]=percentage
    return students