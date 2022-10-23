x = 0
y = 1
count = 0
sum = 0

while count < 6:
    count+=1
    print(x)
    sum += x
    x, y = y, x+y

print(sum)

