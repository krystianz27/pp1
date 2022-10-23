from random import randint
pin = randint(1000, 10000)

count = 0
while count < 3:
    code = int(input("Enter the PIN code: "))
    count += 1
    if code != pin:
        print("Incorrect!")
    else:
        print("Authorization")
        
print("Sorry, your payment card has been blocked.")
    

