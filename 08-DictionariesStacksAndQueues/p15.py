ICAO = {
    "A" : "Alfa",
    "B" : "Bravo",
    "C" : "Charlie"
}

file = open("ICAO.txt", "w", encoding="utf-8")

# file.write(ICAO)

for key, value in ICAO.items():
    file.write(key + " " + value +"\n")


file.close()