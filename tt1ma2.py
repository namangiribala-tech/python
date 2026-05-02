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

# count the numbr f datas 
print("Total number of students:", len(students))

l=[]
#names in students 
for  i in students:
    l.append(i["name"])

#roll in tup
t=()
for i in students:
    t+=(i["roll"],)
print("roll nubers are;",t)

