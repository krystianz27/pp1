import json

with open("test.json") as file:
    data = json.load(file)

for dict in data:
    for key, vvalue in dict.items():
        
