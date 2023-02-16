#Exercise 6.10
favorite_numbers = {
    'Sarah': [7, 2, 6],
    'Michael': 10,
    'John': [3, 5, 78],
    'Emily': 5,
    'Abel': [66, 5, 74]
    }

for number in favorite_numbers.values():
    if isinstance(number, (list, tuple)):
        prt = len(number)
        print(prt)
    else:
        print(1)

#print(f"Abel's favorite number is {favorite_numbers['Abel']}")