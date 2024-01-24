people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f1(person):
    return person["name"]

people.sort(key=f1)

print(people)

def f2(person):
    return person["house"]

people.sort(key=f2)

print(people)
