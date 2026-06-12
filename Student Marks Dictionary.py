students = {
    "Divya": 78,
    "Apurva": 92,
    "Arpit": 40,
    "Rahul": 95
}

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Highest Marks:", highest, students[highest])
print("Lowest Marks:", lowest, students[lowest])

print("Students scoring more than 85:")
for name, marks in students.items():
    if marks > 85:
        print(name, marks)