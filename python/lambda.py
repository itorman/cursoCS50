people = [
    {"name": "Sohn", "age": 20},
    {"name": "Jane", "age": 25},
    {"name": "Rack", "age": 30},
]
# def name(person):
#     return person["age"]

people.sort(key=lambda person: person["age"]);
print(people)