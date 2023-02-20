sandwich_orders = ['tuna', 'bacon', 'strawberry', 'jellyfish']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nHere is the list of sandwichs made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")