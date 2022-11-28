import json

with open("test.json") as file:
    data = json.load(file)

for dict in data:
    for key, value in dict.items():
        d

