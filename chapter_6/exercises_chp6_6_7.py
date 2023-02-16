#Exercise 6.7
person_1 = {
    'first_name': 'Lucilene',
    'last_name': 'Grigorio',
    'age': 58,
    'city': 'Anápolis',
    }

person_2 = {
    'first_name': 'Mak',
    'last_name': 'Jesus',
    'age': 25,
    'city': 'Anápolis',
}

person_3 = {
    'first_name': 'Caio',
    'last_name': 'Jesus',
    'age': 20,
    'city': 'Anápolis',
}

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n")