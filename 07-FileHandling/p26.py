import re

file = open("tekst.txt", encoding="UTF-8")
tekst = file.read()
file.close()

words = re.findall(r"\w+", tekst)
# print(words)

def filter_words(n):
    if len(n) >=6:
        return True
    else:
        return False

words_list = list(filter(filter_words, words))
# print(words_list)

for word in words_list:
    print(word)