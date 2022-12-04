file = open("tekst15.txt", encoding="UTF-8")

i = 0
while i < 5:
    print(file.readline(), end="")
    i += 1
    if i == 5:
        key = input("Press Enter to read the next five lines.")
        if key == "":
            i = 0

file.close()

# x = file.readline()
# print(x)