student = {
    "name": "Arpit",
    "age": 21,
    "course": "Python"
}

print(student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

numbers = [12, 45, 7, 23, 56, 89, 34]

largest = max(numbers)
smallest = min(numbers)

numbers.sort(reverse=True)
second_largest = numbers[1]

print("Largest:", largest)
print("Second Largest:", second_largest)
print("Smallest:", smallest)