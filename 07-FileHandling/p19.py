file = open("numbers.txt", "w", encoding="UTF-8")

for i in range(1,51):
    file.write(str(i) + "\n")

file.close()