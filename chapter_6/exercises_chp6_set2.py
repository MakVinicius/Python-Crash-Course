#Exercise 6.4
favorite_numbers = {
    'Sarah': 7,
    'Michael': 10,
    'John': 3,
    'Emily': 5,
    'Abel': 6,
    }

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")

#Exercise 6.5
rivers = {
    'nile': 'Egypt', 
    'Amazon River': 'Brasil', 
    'Yellow River': 'China',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("The rivers mentioned are: ")
for river in set(rivers.keys()):
    print(river.title())

print("The countries mentioned are: ")
for country in set(rivers.values()):
    print(country.title())


#Exercise 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
people = ['adam', 'susane', 'trace', 'jen', 'sarah']

print("\n")
for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()} thank you for responding the poll.")
    else:
        print(f"Hi {name.title()}, I strongly recommend you take our poll.")
