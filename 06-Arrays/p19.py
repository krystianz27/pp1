array = [15, 8, 31, 47, 2, 19]
sum = 0
i = 0
while i < len(array):
    sum += array[i]
    i+=1

mean = sum / len(array)

print(sum)
print(mean)