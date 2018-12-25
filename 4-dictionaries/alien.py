alien_0 = {'color': 'green', 'points': 5}
alien_0['color']
alien_0['x_position'] = 0
alien_0['y_position'] = 200
alien_0['speed'] = 'fast'

print(alien_0)
print("Moving alien")
alien = alien_0
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x position: {alien_0['x_position']}")

# Deleting dictionary items
del alien_0['color']
alien_0

favourite_languages = {
    'jon': 'python',
    'sarah': 'c',
    'jake': 'python'
    }
print(f"Sarah's favourite language is {favourite_languages['sarah'].title()}.")

glossary = {
    'variable': 'somewhere to store some stuff',
    'listssss': 'a collection of multiple things',
    'dictionary': 'a mapping between multiple pairs of things'
}

# Looping through keys and values
for term, definition in glossary.items():
    print(f"{term}\t\t{definition}\n")

# Looping through keys
for term in favourite_languages:
    print(term)

for term in favourite_languages.keys():
    print(term)

# Looping through values
for value in favourite_languages.values():
    print(value)

for value in sorted(favourite_languages.values()):
    print(value)

for value in set(favourite_languages.values()):
    print(f"n{value}")
