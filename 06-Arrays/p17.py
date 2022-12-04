from random import randint
array = [randint(0, 10) for x in range(10)]
print(array)

for x in range(len(array)):
    array[x] *= array[x]

print(array)
