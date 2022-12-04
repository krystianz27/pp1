# a.	the array
# b.	size of the array (number of rows and columns)
# c.	value 5 from the array
# d.	value 3 from the array
# e.	second row of the array as below:
# 9 0 3
# f.	all values from the array as below:
# 2 5 4 
# 9 0 3
# g.	last column of the array as below:
# 4
# 3

arr = [[2,5,4],[9,0,3]]

print(arr)

print(f"Row {len(arr)} Columns {len(arr[0])}")

print(arr[0][1])

print(arr[1][2]) 

print(arr[1][:]) #e
print(arr[1]) #e

print(arr[0], '\n' , arr[1])

print(f"{arr[0][2]}\n{arr[1][2]}")

def f():
    x = f"{arr[0]} \n{arr[1]}"
    return x

print(f())