#Exercise 5.1 and 5.2
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

car = 'BMW'
print("Is car == 'bmw'? I predict True.")
print(car.lower() == 'bmw')

age = 22
print("Is age >= 18? I predict True.")
print(age >= 18)

age_0 = 22
age_1 = 18
print("Is age >= 18 for both persons? I predict True.")
print(age_0 >= 18 and age_1 >= 18)

cars = ['subaru', 'bmw', 'audi', 'tesla', 'mercedes']
print("Is tesla in cars? I predict True.")
print('tesla' in cars)

cars = ['subaru', 'bmw', 'audi', 'tesla', 'mercedes']
print("Is toyota not in cars? I predict True.")
print('toyota' not in cars)