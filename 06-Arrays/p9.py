# An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. 
# Create a program that displays the longest name (consisting of the largest number of characters). 
# Sample result:

arr = ["Genowefa", "Onfury", "Celestyna","Alojzy", "Pankracy"]

arr2 = []

for name in range(len(arr)):
    arr2.append(len(arr[name]))

print(f"{arr[arr2.index(max(arr2))]} - {max(arr2)}")