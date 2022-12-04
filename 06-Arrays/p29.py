from random import randint

array = [randint(0, 100) for k in range(10)]
print(array)

number = int(input("Enter a number: "))
value = 0

for x in array:
    if x > number:
        value +=1

print(value)