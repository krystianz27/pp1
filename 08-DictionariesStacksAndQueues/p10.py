# 10. Create an array with 5 dictionaries, each containing a country and its population. 
# Then, using ‘while’ loop, display the array contents

table = [
    {"Poland" : 40},
    {"Germany": 83},
    {"France" : 68},
    {"Norway" : 5},
    {"Russia" : 143}
]

# print(table)

i = 0
while i < len(table):
    print(table[i])
    i+=1

