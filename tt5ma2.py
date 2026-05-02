import ttfun as tf
students = [
    { "roll" : 101, "name": "Ameet", "branch": "CSE", "marks": (78, 67, 89)},
    { "roll" : 102, "name": "Riyaa", "branch": "CSE", "marks": (88, 91, 76)},
    { "roll" : 103, "name": "Suman", "branch": "ECE", "marks": (92, 81, 74)},
    { "roll" : 104, "name": "Priya", "branch": "EEE", "marks": (65, 69, 72)},
    { "roll" : 107, "name": "Ameet", "branch": "CSE", "marks": (78, 67, 89)},
    { "roll" : 108, "name": "Diyaa", "branch": "EEE", "marks": (85, 81, 76)},
    { "roll" : 109, "name": "Rohan", "branch": "ECE", "marks": (37, 87, 70)},
    { "roll" : 110, "name": "Sriya", "branch": "EEE", "marks": (65, 66, 72)},
    { "roll" : 111, "name": "Kusal", "branch": "ME",  "marks": (88, 73, 84)},
    { "roll" : 105, "name": "Kunal", "branch": "CSE", "marks": (91, 73, 84)},
    { "roll" : 106, "name": "Meera", "branch": "ME",  "marks": (58, 82, 55)},
    { "roll" : 112, "name": "Manoj", "branch": "ME",  "marks": (78, 73, 65)},
]

oc=students.copy()
# for i  in students:
#     total=sum(i["marks"])
#     percentage=(total/300)*100
#     i["percentage"]=percentage
bc=tf.percentage(students)


#correction marks and recalculate the percentage of the studets whise a=marks RE changed 

cormark={    #corrected markswith correspoding roll numbers
104: (70, 75, 80),
106: (92, 97, 97)
}


for i in oc:
    roll=i["roll"]
    if roll in cormark:
        i["marks"]=cormark[roll]

#perentage recalculation
tf.percentage(oc)

#check the marking list of the students after correction

if oc==bc:
    print("no changes in the percentage after correction of marks")
else:
    print("changes in the percentage after correction of marks")



