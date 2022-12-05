def f(array2D):
    new_array = []
    
    for y in range(len(array2D[1])):
        a = 0
        for x in range(len(array2D)):
            a += array2D[x][y]

        new_array.append(a)
    return new_array




# print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))
# print(f([[3,6,2,7], [9,5,4,0], [2,8,0,9], [1,1,1,1]]))
