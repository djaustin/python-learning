prompt = "Welcome to Parrot. It does what it says on the box.\nType 'quit' to stop.\n"
active = True
while active:
    message = input(prompt)

    if message.lstrip().rstrip() == 'quit':
        active = False
    else:
        print(message)
