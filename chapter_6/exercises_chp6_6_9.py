#Exercise 6.9
favorite_places = {
    'Kate': ['Rio', 'Guanabara'],
    'John': 'Florianópolis',
    'Emily': ['Paris', 'Veneza', 'Rome']
}


for key, value in favorite_places.items():
    if len(value) > 3:
        print(f"{key.title()}'s favorite places are: ")
        print(f"\t{value}")
    else:
        print(f"{key.title()}'s favorite places are: ")
        for place in value:
            print(f"\t{place}")
    print("\n")