def f(arr):
    for x in range(len(arr)-1):
        # print("x", x) #> 0, 1
        for y in range(len(arr[x])):
            # print(y)  #> 0,1,2, 0,1,2

            if arr[0][y] != (1/(x+2))*arr[x+1][y]:
                return False
    return True



# print(f([[1,2,3],[2,4,6],[3,6,9]]))
# print(f([[1,2],[2,4]]))
# print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
# print(f([[1,2],[3,6]]))
# print(f([[1,2,3],[2,5,6]]))

