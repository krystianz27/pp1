array1 = [1,0,9,4,6]
array2 = [6,8,3,1,0,5,7]

def median(array):
    array.sort()
    if len(array) %2 == 1:
        index = len(array) // 2
        middle = array[index]
        return middle
    elif len(array) %2 == 0:
        index = len(array) / 2
        middle = array[index -1] + array[index]
        return middle

print(median(array1))
print(median(array2))