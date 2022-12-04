import re

tekst = "To be, or not to be, that is the question"

vowels = re.findall("[aeiou]", tekst)
print(len(vowels))