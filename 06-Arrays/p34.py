array1 = [1,2,3,4,0]
array2 = [1,2,0,3,4,5,6,7,8]

def subset():
    for x in array1:
        if not x in array2:
            return False
    return True

print(subset())