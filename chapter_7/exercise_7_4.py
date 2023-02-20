#Exercise 7.4 Pizza toppings
pizza_topping = ""
while pizza_topping != 'quit':
    pizza_topping = input("\nType your topping for your pizza.\nWhen your done type quit: ")
    if pizza_topping != 'quit':
        print(f"Adding {pizza_topping} to your pizza!")