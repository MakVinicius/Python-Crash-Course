dream_vacation = {}
flag = True

while flag:
    names = input("What is your name? ")
    locations = input("If you could visit one place in the world, where would you go? ")
    continues = input("Would you like to continue adding names? (yes or no): ")

    dream_vacation[names] = locations
    if continues.lower() == 'no':
        flag = False

print("\n--- Results of the poll ---")
for name, location in dream_vacation.items():
    print(f"{name.title()} would like to go to {location.title()}.")