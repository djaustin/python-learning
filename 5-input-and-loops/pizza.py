toppings = []

welcome = "Welcome to Domino's CLI."
prompt = "Please choose a pizza topping\n(Enter 'done' when you have added all your toppings.)\n"

print(welcome)
while True:
    topping = input(prompt)
    if topping == 'done':
        break
    else:
        toppings.append(topping)
        print(f"{topping.capitalize()} has been added to your pizza.\nYour pizza currently has the following toppings: {toppings}")
