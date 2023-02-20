#Exercise 7.1 Rental Car
car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {car.title()}")

#Exercise 7.2 Restaurant seating
group = input("How many people are in your dinner group? ")
group = int(group)
if group > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

#Exercise 7.3 Multiples of Ten
number = int(input("Enter a number and I will tell you if it is multiple of 10: "))

if number % 10 == 0:
    print(f"{number} is multiple of 10.")
else:
    print(f"{number} is not multiple of 10.")