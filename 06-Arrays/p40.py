array1 = [[-38, 19], [5,40], [-7,11], [29,16]]
max = array1[0][0]
min = array1[0][0]
min_index = 0,0
max_index = 0,0

for x in range(len(array1)):
    for y in range(len(array1[x])):
        if array1[x][y] < min:
            min = array1[x][y]
            min_index = x,y        

        elif array1[x][y] > max:
            max = array1[x][y]
            max_index = x,y


print(f"Max value: {max} Row: {max_index[0]} Column: {max_index[1]}")
print(f"Min value: {min} Row: {min_index[0]} Column: {min_index[1]}")

