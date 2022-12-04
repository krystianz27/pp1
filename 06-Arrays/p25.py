array1 = [15, 38, 7, 23, 14] 

number = int(input("Enter a number: "))

def occurs(number, array):
    if number in array: return True

    else: return False

print(occurs(number, array1))