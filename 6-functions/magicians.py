magicians = ['alice', 'bob', 'charlie', 'donald']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for key, magician in enumerate(magicians):
        magicians[key] = magician.title() + ' the Great'
    return magicians

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
