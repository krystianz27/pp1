array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

for x in range(len(array2)):
    if array2[x] in array1:
        array1.remove(array2[x])


print(array1)