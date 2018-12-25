unconfirmed_users = ['alice', 'bob', 'charlie']
confirmed_users = []

while unconfirmed_users: # Conditional check evaluate to true while list is not empty
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nConfirmed Users:")
for user in confirmed_users:
    print(user.title())
