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

tf.percentage(students)

# identidy students with identical total marks and create a dictionary where key is the total marks and value is student names
d={}
for i in students:
    total=sum(i["marks"])
    if total in d:
        d[total].append(i["name"])
    else:
        d[total]=[i["name"]]

print(d)

# detect constantly high performers in all subjects ( more than 75 in all subjects) display their roll numbers and names 
for i in students:
    if all(m>75 for m in i["marks"]):
        print(f"constantly high performer : roll no:{i['roll']}, name:{i['name']}")

# Generate a subject toppers report. Format: {subject index: (student name, marks)}, showing the
# highest scorer for each subject

report={}
for i in range(3): 
    t=max(students,key=lambda x:x["marks"][i])
    report[i]=(t["name"],t["marks"][i])

print("subject toppers report:", report)

# Create dictionary to store average percentage marks of the branches across all the students as {branch
# : average percentage marks} percentage.

branch_totals={}
for i in students:
    branch=i["branch"]
    if branch in branch_totals:
        branch_totals[branch].append(i["percentage"])
    else:
        branch_totals[branch]=[i["percentage"]]

# Calculate average percentage for each branch
branch_averages={}
for branch, percentages in branch_totals.items():
    branch_averages[branch]=sum(percentages)/len(percentages)

print("Average percentage marks by branch:", branch_averages)

# Detect failing students (any mark < 40). Display their names and roll numbers using a list of tuples
failing_students=[]
for i in students:
    if any(m<40 for m in i["marks"]):
        failing_students.append((i["roll"], i["name"]))

print("Failing students (roll no, name):", failing_students)

 #Prepare a dictionary summer quarter that contains the following:
#• Key: Student roll number
#• Value: A list of tuples, where each tuple contains: (i) index of the subject in which the student
#has failed and (ii) mark obtained in that subject

 #Prepare a dictionary summer quarter that contains the following:
#• Key: Student roll number
#• Value: A list of tuples, where each tuple contains: (i) index of the subject in which the student
#has failed and (ii) mark obtained in that subject
summer_quarter={}
for i in students:
    failed_subjects=[]
    for idx, mark in enumerate(i["marks"]):
        if mark<40:
            failed_subjects.append((idx, mark))
    if failed_subjects:
        summer_quarter[i["roll"]]=failed_subjects

print("Summer quarter failing subjects report:", summer_quarter)

#  Calculate the variance and standard deviation of marks for each subject. Perform calculations manu
# ally without using any Python libraries
import math
n=len(students)
for i in range(3):
    marks=[s["marks"][i] for s in students]
    mean=sum(marks)/n
    variance=sum((m-mean)**2 for m in marks)/n
    stddev=math.sqrt(variance)
    print(f"Subject {i}: Variance={variance:.2f}, Standard Deviation={stddev:.2f}")

