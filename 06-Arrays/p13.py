array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum = 0

for x in array:
    for y in x:
        # print(y)
        if y % 2 == 0:
            sum += y

print(sum)