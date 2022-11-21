lista = ["Title1", "Title2", "Title3", "Title4", "Title5"]

file = open("Titles.txt", "w")

for title in lista:
    file.write(title + "\n")

file.close()