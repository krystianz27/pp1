import csv

file = open("students.csv", "r")

tekst = csv.reader(file)
next(tekst)

for x in tekst:
    if int(x[2]) < 30:
        print(x[0], x[1], x[4])



