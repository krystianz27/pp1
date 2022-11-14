# 10.	An array contains integer numbers. Create a program that calculates 
# and displays the number of even and odd values in the array. Use the “while” loop statement.

import random

arr = [random.randint(0, 10) for i in range(20)]
even = 0
odd = 0
arr_even = 0
arr_odd = 0
index = 0

while index < len(arr):
    if int(arr[index]) %2 ==0:
        arr_even+=1
    else:
        arr_odd+=1
    index +=1

print(arr_even, arr_odd)
        



# print(arr)

