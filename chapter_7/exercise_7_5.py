#Exercise 7.5 Movie tickets
age = 0
while age != quit:
    age = input("\nEnter your age to know the ticket price.\nIf you want to get out type quit: ")
    if age == 'quit':
        break
    elif int(age) < 3:
        print("The ticket is free!")
    elif int(age) < 13:
        print("The ticket price is $10.")
    elif int(age) > 12:
        print("The ticket price is $15.")