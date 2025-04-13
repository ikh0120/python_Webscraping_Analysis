arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

result = list(map(lambda x: x[0] + x[1], zip(arr1, arr2)))

print(result)
