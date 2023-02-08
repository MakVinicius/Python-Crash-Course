#Exercise 3.4
guests = ['jordan', 'leonard', 'curry', 'lebron', 'durant']
message = f"I'd like to invite you to dinner {guests[0].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[1].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[2].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[3].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[4].title()}"
print(message)

#Exercise 3.5
cant_makeit = guests[0]
print(f"The guest {cant_makeit.title()} couldn't make to dinner.")

guests[0] = 'murant'
message = f"I'd like to invite you to dinner {guests[0].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[1].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[2].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[3].title()}"
print(message)
message = f"I'd like to invite you to dinner {guests[4].title()}"
print(message)

#Exercise 3.6
guests.insert(3, 'doncic')
guests.append('Antetokounmpo')
guests.insert(0, 'tatum')
print(guests)

#Exercise 3.7
print("Hello everyone, the dinner table only has 2 chairs, so some people have been cut off from the list.")
cant_makeit = guests.pop(0)
message = f"Hello {cant_makeit.title()} I'm sorry to inform you that the dinner has been canceled due to not having enough seats for everyone."
print(message)
cant_makeit = guests.pop(0)
message = f"Hello {cant_makeit.title()} I'm sorry to inform you that the dinner has been canceled due to not having enough seats for everyone."
print(message)
cant_makeit = guests.pop(0)
message = f"Hello {cant_makeit.title()} I'm sorry to inform you that the dinner has been canceled due to not having enough seats for everyone."
print(message)
cant_makeit = guests.pop(0)
message = f"Hello {cant_makeit.title()} I'm sorry to inform you that the dinner has been canceled due to not having enough seats for everyone."
print(message)
cant_makeit = guests.pop(0)
message = f"Hello {cant_makeit.title()} I'm sorry to inform you that the dinner has been canceled due to not having enough seats for everyone."
print(message)
cant_makeit = guests.pop(0)
message = f"Hello {cant_makeit.title()} I'm sorry to inform you that the dinner has been canceled due to not having enough seats for everyone."
print(message)

del guests[0]
del guests[0]

print(guests)