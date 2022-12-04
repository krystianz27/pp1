file1 = open("tekst15.txt")

content = file1.read()
file1.close()

file2 = open("copy.txt", "w")
file2.write(content)
file2.close()

