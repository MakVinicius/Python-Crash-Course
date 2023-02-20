sandwich_orders = ['pastrami', 'tuna', 'bacon', 'pastrami', 'strawberry', 'jellyfish', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)