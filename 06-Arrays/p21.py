arr1 =["water","book","sky"]   
arr11 = ["water","book","sky"]
arr2 = [True,False]   
arr22 = [True,False,True]
arr3 = [5,3,1]   
arr33 = [5,3,1]
arr4 = [3,2,1]   
arr44 = [3,2]


def compare(array1, array2):
    # if array1 == array2:
    #     return True
    # else:
    #     return False    #sposob 2 nizej

    if len(array1) != len(array2):
        return False
    for x in range(len(array1)):
        if array1[x] != array2[x]:
            return False
    return True


print(compare(arr1, arr11))
print(compare(arr2, arr22))
print(compare(arr3, arr33))
print(compare(arr4, arr44))