def transpose_matrix(m):
# x = 0
# y = len(m)-1
# while x < len(m):
#     m[x][x], m[x][y] = m
    z = len(m) // 2 
    for x in range(1):
        for y in range(len(m[x])):
            m[x][y], m[y][x] = m[y][x], m[x][y] 
            # m[z][z+1], m[z+1][z] = m[z+1][z], m[z][z+1]
    return m

    
array1 = [[1,2,3], [4,5,6], [7,8,9]]
array2 = [[1,2,3,4,5], [6,7,8,9,0]]

# print(transpose_matrix(array1))
k = transpose_matrix(array2)
print(k)



# 1 2 3
# 4 5 6
# 7 8 9




# b.	1 2 3 4 5
# 6 7 8 9 0
# c.	5 6 7 8
