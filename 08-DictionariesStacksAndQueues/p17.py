import json
file = open("euro.json", encoding="utf-8")
content = json.load(file)

# print(content)
print("Date         ", "Buying Rate   ", "Selling Rate")
print("=========================================")
# for line in content:
#     print(["rates"])
#     # print(line)

for line in content["rates"]:
    x = line["ask"]
    x = str(x)
    if len(x) <=5:
        x += "0"
    # print(x)
    # print(round(x,4))
    print(line["effectiveDate"], "  ",x ,  "       ", line["bid"])
