dream_vacations = {}

active = True

while active:
    name = input("What is your name?: ")
    destination = input("What is your dream vacation?: ")
    dream_vacations[name] = destination
    active = input("Would you like to continue polling? (y/n) ") == 'y'

for name, destination in dream_vacations.items():
    print(f"{name.title()} would like to go on vacation to {destination}")
