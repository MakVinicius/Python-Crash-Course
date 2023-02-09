#Exercise 4.3
numbers = []
for number in range(1, 21):
    numbers.append(number)

print(f"{numbers}\n")

#Exercise 4.6
numbers = []
for number in range(1, 21, 2):
    print(number)

print("\n")

#Exercise 4.7
numbers = []
for number in range(3, 31, 3):
    print(number)

print("\n")

#Exercise 4.8
numbers = []
for number in range(1, 11):
    number_mod = number ** 3
    print(number_mod)

print("\n")

#Exercise 4.9
numbers = [number ** 3 for number in range(1, 11)]
print(numbers)
print("\n")