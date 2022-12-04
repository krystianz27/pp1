array = [[0,0,0],[0,0,0],[0,0,0]]
index = 0 

for x in range(len(array)):
    # for y in range(len(array[x])):
    array[x][x] = 1

print(array)
