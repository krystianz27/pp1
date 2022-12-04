file1 = open("tekst15.txt")

content = file1.read()

file1.close()

print(content)


file2 = open("copylines.txt", "a")
for word in content:
    file2.write(word)

# file2.write("\n")

file2.close()

# print(content[-2:])