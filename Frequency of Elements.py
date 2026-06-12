def count_frequency(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for key, value in freq.items():
        print(key, "->", value, "times")


arr = [1, 2, 2, 3, 1, 4, 2]
count_frequency(arr)