import json

film = {
    "title" : "xyz",
    "year" : 2022,
    "director" : "abc",
    "director" : "abc",
    "director" : "abc",
    "director" : "abc",
    "director" : "abc",
    "rate" : 9,
    "rate" : 9,
    "rate" : 9,
    "genre" : "comedy",
    "bla" : {"nested1" : "nested2",
    "nested3" : "nested4"
    }
}

with open("student.json", "r") as file:
    json.dump(film, file, indent=2)