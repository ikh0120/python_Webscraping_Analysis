arr1 = [1, 2, 3]
arr2 = [10, 20, 30]

result = list(zip(arr1, arr2))

for first, second in result:
    print(f"{first} {second}")