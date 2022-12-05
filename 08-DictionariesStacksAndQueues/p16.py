import json

file1 = open("students.json", encoding="utf-8")
content1 = json.load(file1)
file1.close()
print(content1)

file2 = open("limited.json", "w", encoding="utf-8", newline="")

for line in content1:
    del line["gender"]
    del line["age"]
    del line["year"]
    del line["email"]

json.dump(content1, file2, indent=2)


