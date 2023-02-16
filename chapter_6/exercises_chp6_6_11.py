#Exercise 6.11
cities = {
    'Paris': {
        'country': 'France',
        'population': 17_000_000,
        'fact': 'has the Eiffel tower',
    },
    'Washington': {
        'country': 'USA',
        'population': 25_000_000,
        'fact': 'It is the capital of USA',
    },
    'Rome': {
        'country': 'Italy',
        'population': 15_000_000,
        'fact': 'It is where the Pope lives',
    },
}

for key1, value1 in cities.items():

    print(f"\nSome information about {key1.title()}:")
    for key2, value2 in value1.items():    
        print(f"\tIts {key2} is {value2}.")