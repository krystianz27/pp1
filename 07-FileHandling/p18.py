file2 = open("MeatandFish.txt", encoding="UTF-8")            #content3 to string i zapisuje po kazdym znaku
content2 = file2.read()
file2.close()

file3 = open("GrainsAndBread.txt", encoding="UTF-8")
content3 = file3.read()
file3.close()

file1 = open("shoppinglist.txt", "w", encoding="UTF-8")
content1 = content2 + content3
print(content1)

for word in content1:
    file1.write(word)

file1.close()






# file2 = open("MeatandFish.txt", encoding="UTF-8")                        #teraz content1 to jest lista i zapisuje po wyrazach
# content2 = file2.readlines()                                             #content2 i content3 to lista
# file2.close()

# file3 = open("GrainsAndBread.txt", encoding="UTF-8")
# content3 = file3.readlines()
# file3.close()

# file1 = open("shoppinglist.txt", "w", encoding="UTF-8")
# content1 = content2 + content3
# print(content1)

# for word in content1:
#     file1.write(word)

# file1.close()
