import csv

# file1 = open("students.csv")
# tekst1 = csv.reader(file1)
# # file1.close()
# # print(tekst1)
# next(tekst1)

# file2 = open("students2.csv", "w", newline="")
# tekst2 = csv.writer(file2, delimiter=",")


# for row in tekst1:
#     tekst2.writerow(row)
#     print(row)





file1 = open("students.csv")
file2 = open("students3.csv", "w", newline="")
csv_reader = csv.DictReader(file1)
fieldnames = ["first_name", "last_name", "age", "gender", "email"]
csv_writer = csv.DictWriter(file2, fieldnames=fieldnames)
csv_writer.writeheader()    #dodaje naglowek przy slowniku
for row in csv_reader:
    # print(row)
    # del row["email"]     
    csv_writer.writerow(row)