def conv(array):
    new_array = []
    for x in array:
        for y in x:
            new_array.append(y)
    return new_array

array1 = [[1,2], [3,4]]
array2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]



print(conv(array1))
print(conv(array2))
