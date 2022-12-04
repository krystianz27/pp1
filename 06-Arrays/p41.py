from random import randint
array1 = [[randint(0,10) for k in range(5)], [randint(0,10) for k in range(5)], [randint(0,10) for k in range(5)]]

for x in array1:
    for y in x:
        print(y, end=" ")
    print()

# print(array1)
array1[0], array1[len(array1)-1] = array1[len(array1)-1], array1[0]
# print(array1)
print()

for x in array1:
    for y in x:
        print(y, end=" ")
    print()
