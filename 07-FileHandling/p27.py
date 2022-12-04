import re

file = open("grades.txt")

tekst = file.read()

# print(tekst)

digit = re.findall(r"[0-9].[0-9]", tekst)

print(digit)

sum = 0
for x in digit:
    sum += float(x)

avg = sum / len(digit)

print(avg)
    