amount = int(input("Enter the amount in PLN: "))

five = amount // 5
five_rest = amount % 5

two = five_rest // 2
two_rest = five_rest - two*2

one = two_rest // 1

print(f"5 zl - {five} \n2 zl - {two} \n1 zl - {one}")

# print(five)
# print(five_rest)
