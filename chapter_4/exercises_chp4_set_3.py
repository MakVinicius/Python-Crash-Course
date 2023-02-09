#Exercise 4.10
numbers = []
for number in range(1, 21):
    numbers.append(number)
#print(numbers)
number_list = numbers[0:3]
print(f"The first three items in the list are: \n{number_list}")

number_list = numbers[8:11]
print(f"Three items from the middle of the list are: \n{number_list}")

number_list = numbers[-3:]
print(f"The last three items in the list are: \n{number_list}")

#Exercise 4.11
pizzas = ['pepperoni', 'muçarela', 'bacon']
for pizza in pizzas:
    print(f"{pizza.title()} pizza is the best!")

#print("I really like pizza and it shouldn't be a surprise of how much I love them.\n")
friend_pizzas = pizzas[:]
pizzas.append('calabresa')
friend_pizzas.append('portuguesa')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
