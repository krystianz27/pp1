import re

tekst = "To be, or not to be, that is the question"

x = re.split(r"\s", tekst)
y = re.findall(r"\w+", tekst)

print(len(x))

# print(y)
print(len(y))