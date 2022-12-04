from random import randint
array1 = [[randint(0,10) for k in range(5)], [randint(0,10) for k in range(5)], [randint(0,10) for k in range(5)]]

for x in array1:
    for y in x:
        print(y, end=" ")
    print()


for x in range(len(array1)):

    array1[x][0], array1[x][len(array1[x])-1] = array1[x][len(array1[x])-1], array1[x][0]



# print(array1)
# print(array1)
print()

for x in array1:
    for y in x:
        print(y, end=" ")
    print()
