file = open("numbers.txt")

numbers = file.readlines()
sum = 0

for number in numbers:
    number = int(number)
    sum +=number
    print(number)

# print(numbers)
print("Sum:", str(sum))

file.close()





# for number in file:
#     number = int(number)
#     sum +=number
#     print(number)

# print("Sum:", str(sum))