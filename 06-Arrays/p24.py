array1 = [2, 4, 3, 2, 5, 8, 1, 9, 8]
array2 = []

for x in range(len(array1)):
    if array1[x] %2 == 1:
        array2.append(array1[x])          #1 sposob
print(array2)


# index = 0
# while index < len(array1):
#     if array1[index] %2 == 0:
#         array1.pop(index)
#         index -= 1
#     index+=1
# print(array1)                  #2sposob

