from random import randint

dice = randint(1,6)
answear = 0
print("Guess the number from 1 to 6")

while answear is not dice:
    answear = int(input("Enter a number: "))
    
print(True)