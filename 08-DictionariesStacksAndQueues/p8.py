person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }


# Then, create a program and do the following tasks:
# a.	Display contents of the dictionary
# b.	Display name
# c.	Display hobby
# d.	Change surname to Nowak
# e.	Change person's marriage status
# f.	Add gender: male
# g.	Add a new hobby: bicycle
# h.	Add work phone to existing phones: 313131444

print(person)
print(person["name"])
print(person["hobby"])
person["surname"] = "Nowak"
print(person)
person["married"] = False
print(person)

person["gender"] = "male"
print(person)

person["hobby"] += ["bicycle"]
print(person["hobby"])

person["phone"]["workphone"] = "313131444"

print(person)