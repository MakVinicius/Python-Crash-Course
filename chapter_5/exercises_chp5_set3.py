#Exercise 5.8 and 5.9
users = ['admin', 'Brenda', 'Michael', 'John', 'Michele']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for loggin in again.")
else:
    print("We need to find some users!")


#Exercise 5.10
print("\n")
current_users = ['admin', 'brenda', 'michael', 'john', 'michele']
new_users = ['Hitch', 'Mark', 'Ana', 'Brenda', 'Michele']
low_new_users = []

for user1 in new_users:
    low_new_users.append(user1.lower())

for user in low_new_users:
    if user in current_users:
        print(f"Username {user} is already taken. Enter a new username.")
    else:
        print(f"Username {user} is available.")


#Execise 5.11
print("\n")
numbers = []

for i in range(1,10):
    numbers.append(i)

for j in numbers:
    if j == 1:
        print(f"{j}st")
    elif j == 2:
        print(f"{j}nd")
    elif j == 3:
        print(f"{j}rd")
    else:
        print(f"{j}th")