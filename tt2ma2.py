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

# calculat ettal and percentage of every student 
for i  in students:
    total=sum(i["marks"])
    percentage=(total/300)*100
    print(f"Student Name: {i['name']}, Total Marks: {total}, Percentage: {percentage:.2f}%")

# find the grade of the students and add it to it 
for i in students:
    total=sum(i["marks"])
    percentage=(total/300)*100
    if percentage >= 90:
        grade = 'O'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 40:
        grade = 'P'
    else:
        grade = 'F'
    i['grade'] = grade

# student grade as per the nput rol nuber 
rollno=int(input("enter the roll number you want to see the grade: "))
for i in students:
    if i["roll"]==rollno:
        print(f"student name:{i["name"]}, roll number:{rollno}, grade{i["grade"]}")

#prtint the students nme with the grade as iput 
g=input("enter the grade you want to see the student names: ").upper()
for i in students:
    if i["grade"]==g:
        print(i["name"])

