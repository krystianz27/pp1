name = input("Input a filename: ")

file = open(name)

i = 0
for line in file:
    i+=1 

file.close()

print("Filename:", name)
print("Number of lines:", i)