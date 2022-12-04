tekst = input("Enter your: name, university, field separated by comma ")
tekst.strip()
tekst1 = tekst.split(",")
print(tekst)
print(tekst1)


file = open("tekst10.txt", "w")

for name in tekst1:
    file.write(name.strip() + "\n")

# file.write('Krystian \n')
# file.write('UEK \n')
# file.write('Informatyka \n')

file.close()
