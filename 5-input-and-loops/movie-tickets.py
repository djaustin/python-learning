print("Welcome to the Cinema!\n(Enter 'quit' to exit the program)")
prompt = "Please enter your age to receive a ticket price:\n"

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        age = int(message)
        if age < 3:
            cost = 0
        elif age < 12:
            cost = 10
        else:
            cost = 15

        print(f"Your ticket costs £{cost}")
