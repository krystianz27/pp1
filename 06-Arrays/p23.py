array1 = [32, 6, 73, 4, 99, 17]

def bubblesort(array):
    for y in range(len(array)):
        for x in range(len(array)-1):
            if array[x] > array[x+1]:
                array[x+1], array[x] = array[x], array[x+1]
    
    return array

print(bubblesort(array1))