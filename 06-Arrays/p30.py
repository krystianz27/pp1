from random import randint
array = [randint(0,10) for k in range(10)]
print(array)

def minmax(array):
    array.sort()
    array2 = []
    array2.append(array[0]) 
    array2.append(array[len(array)-1]) 
    return array2

print(minmax(array))