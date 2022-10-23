a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("*" * a)
for x in range(b-2):
    print("*" + " "*(a-2) + "*")
print("*" * a)