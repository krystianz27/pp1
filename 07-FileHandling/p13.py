# f = open("filename.txt")
# for line in f:
#      print(line, end="")
# f.close()


with open("filename.txt") as f:
    for line in f:
        print(line, end="")

# f.close()