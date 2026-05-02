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

# for i  in students:
#     total=sum(i["marks"])
#     percentage=(total/300)*100
#     i["percentage"]=percentage
tf.percentage(students)


#identify toppers
mxpe=max(i["percentage"] for  i in students)
print(f"topper is {mxpe} and details are:", [i for i in students if i["percentage"]==mxpe])

#identify the branch toppers 
branches=set()
for i in students:
    branches.add(i["branch"])

for i in branches:
    for j in students:
        ma=0
        n=0
        if j["branch"]==i and j["percentage"]>ma:
            ma=j["percentage"]
            n=j["name"]
    print(f"topper in{i} brranch is {n} with percentage{ma}")

# decrreasing orf=der ububble sort of students based on percentage

for i in range(n):
    for j in range(0, n - i - 1):
        if students[j]["percentage"] < students[j + 1]["percentage"]:
            students[j], students[j + 1] = students[j + 1], students[j]

print("Top 10 Students by Percentage (Descending Order):\n")
for i in range(10):
    s = students[i]
    print(
        s["roll"], "-", s["name"],
        "| Branch:", s["branch"],
        "| Percentage:", round(s["percentage"], 2), "%"
    )

#imput roll number from user and display student details
rollno=int(input("enter the roll number to see the student details: "))
for i in students:
    if i["roll"]==rollno:
        print(f"student details are: roll no:{i['roll']}, name:{i['name']}, branch:{i['branch']}, marks:{i['marks']}, percentage:{i['percentage']:.2f}%")

