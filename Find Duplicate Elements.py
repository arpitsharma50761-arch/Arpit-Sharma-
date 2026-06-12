def find_duplicates(arr):
    duplicates = set()

    for i in arr:
        if arr.count(i) > 1:
            duplicates.add(i)

    print("Duplicate elements are:")
    for i in duplicates:
        print(i)


arr = [10, 20, 30, 20, 40, 10, 50, 30, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
find_duplicates(arr)