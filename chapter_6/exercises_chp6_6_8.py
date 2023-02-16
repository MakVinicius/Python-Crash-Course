#Exercise 6.8
pet_1 = {
    'owner': 'Lucilene',
    'type': 'dog',
    'age': 8,
    'city': 'Anápolis',
    }

pet_2 = {
    'owner': 'Mak',
    'type': 'cat',
    'age': 5,
    'city': 'Anápolis',
}

pet_3 = {
    'owner': 'Caio',
    'type': 'turtle',
    'age': 2,
    'city': 'Anápolis',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("\n")