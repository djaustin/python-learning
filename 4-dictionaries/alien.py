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
