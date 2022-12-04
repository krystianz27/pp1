array = [15, 8, 31, 47, 2, 19]

index = len(array)-1

for item in array:
    print(item, end=" ")

print()


for item in range(len(array)-1 , -1, -1):
    print(array[item], end=" ")
    # print(item)

print()

array2 =array.copy()
array2.reverse()
# print(array2)
for item in range(len(array2)):
    print(item, end=" ")
    print(array2[item], end=" ")
