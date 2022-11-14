# An array contains numbers: -15, 8, -31, 47, -2, 19. 
# Create a program that finds and displays the maximum and minimum number. 
# Do not use available functions.

arr = [-15, 8, -31, 47, -2, 19]

maximum = arr[0]
minimum = arr[0]

for item in arr:
    if item >= maximum:
        maximum = item

    if item <= minimum:
        minimum = item
print(f"Maksimum: {maximum} Minimum: {minimum}")

# for item in arr:
#     if item <= minimum:
#         minimum = item
# print(minimum)