import json

film = {
    "title" : "xyz",
    "year" : 2022,
    "director" : "abc",
    "rate" : 9,
    "genre" : "comedy",
    "bla" : {"nested1" : "nested2",
    "nested3" : "nested4"
    }
}

with open("favourite.json", "w") as file:
    json.dump(film, file, indent=4)