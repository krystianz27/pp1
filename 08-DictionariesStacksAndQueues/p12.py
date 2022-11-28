import json

film = {
    "title" : "xyz",
    "year" : 2022,
    "director" : "abc",
    "rate" : 9,
    "genre" : "comedy"
}

with open("favourite.json", "w") as file:
    json.dump(film, file, indent=2)