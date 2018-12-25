names = ['adam', 'brandon', 'carl', 2]

# Accessing elements notice the method of accessing the final element of the list
print(names[0])
print(names[1])
print(names[-1])

# Iterate over all list elements using for-in syntax
for name in names:
    print("Hello " + str(name).title() + "!")


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Editing an element of a list is done by accessing the position and assigning a new value to it
# Lists are mutable
motorcycles[1] = 'ducati'
print(motorcycles)

# Adding to a list
motorcycles.append("triumph")
motorcycles.insert(1, "harley")
motorcycles

# Delete an element by index
del motorcycles[0]

guest_list = ['Hawking', 'Fry', 'Einstein']
for guest in guest_list:
    print(f"Hello {guest}, would you like to come to dinner?")

print(f"Unfortunately, {guest_list[1]} cannot make it tonight.")

guest_list[1] = "Attenborough"

for guest in guest_list:
    print(f"Hello {guest}, would you like to come to dinner?")


print(f"Hello {guest_list[0]}, {guest_list[1]}, {guest_list[2]}. I have been able to secure a larger tablet so we will be expanding our group")

guest_list.insert(0, 'Obama')
guest_list.insert(1, 'Kennedy')
guest_list.append('Mathers')

for guest in guest_list:
    print(f"Hello {guest}, would you like to come to dinner?")

print("I am now only able to seat two guests, sorry!")

for i in range(len(guest_list)-2, 0, -1):
    print(f"Hi {guest_list.pop(i)}, I'm really sorry but you're off the list!")

print(guest_list)

for guest in guest_list:
    print(f"Good news, {guest}! you're still on for dinner!")

del guest_list[0]
del guest_list[0]

print(motorcycles)

print(sorted(motorcycles))

print(motorcycles)

print(motorcycles.sort())
print(motorcycles)

print(guest)

squares = [value**2 for value in (range(1,11))]
squares

# Slicing a list
numbers = list(range(0,11))
numbers
numbers[0:3]
numbers[:3]
numbers[3:]
numbers[3:5]

for number in numbers[-3:]:
    print(number)


# Copying a list
numbers2 = numbers[:]
numbers2
del numbers[0]
numbers
numbers2


# Checking values in a list
print(1 in numbers)
print(1 not in numbers)

# Checking if list is empty
if numbers:
    print("There are numbers")
else:
    print("There are no numbers")
