import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

temperatures = re.findall("\d{2}",message)

print(temperatures)

sum = 0
for x in temperatures:
    sum += int(x)

average = sum / len(temperatures)
print(average)
