data = (5, 10, 15, 20, 25, 30, 35)

count = 0
for i in data:
    if i % 5 == 0:
        count += 1

total = sum(data)
average = total / len(data)

print("Divisible by 5:", count)
print("Sum:", total)
print("Average:", average)