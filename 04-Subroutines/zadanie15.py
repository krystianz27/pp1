from mymath import read_number
from mymath import generate_number
from random import randint

# n = int(input("Enter a number: "))

number = generate_number()
print(number)

n = int(input("Enter a number: "))

if n == number:
    print("You guessed the number")