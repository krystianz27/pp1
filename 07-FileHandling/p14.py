name = input("Input a filename: ")

file = open(name)

i = 0
for line in file.readlines():
    i+=1 


print("Filename:", name)
print("Number of lines:", i)