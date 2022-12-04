array = [[True,False,],[True,True],[False,False]]
print(array)

for x in range(len(array)):
    for y in range(len(array[x])):
        # print(y)
        if array[x][y] == True:
            array[x][y] = False

        elif array[x][y] == False:
            array[x][y] = True

print(array)

