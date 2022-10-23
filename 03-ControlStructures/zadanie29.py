count = 0
sum = 0
average = 0

while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    count +=1
    sum = sum + number
    average = sum / count

print(f"Quantity: {count}, Sum: {sum}, Mean: {average}")