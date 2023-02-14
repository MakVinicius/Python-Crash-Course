#Exercise 5.3
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points.")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points.")

#Exercise 5.4
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

#Exercise 5.5
print("\n")
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points.")
elif alien_color == 'yellow':
    print("You just earned 10 points.")
elif alien_color == 'red':
    print("You just earned 15 points.")

#Exercise 5.6
print("\n")
age = 25

if age < 2:
    print("You are just a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are an elder.")