from random import randint
array1 = [randint(0,10) for k in range(10)]
array2 = []

for x in array1:
    if x % 2 == 0:
        array2.append(x)

for x in array1:
    if x % 2 == 1:
        array2.append(x)


print(array1)
print(array2)
