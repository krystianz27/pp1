from random import randint

file = open("numbers2.txt", "w", encoding="UTF-8")

for i in range(50):
    file.write(str(randint(100, 999)) + "\n")

file.close()
