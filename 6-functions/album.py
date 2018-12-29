def make_album(artist, title, tracks=None):
    album = {}
    album['artist'] = artist
    album['title'] = title

    if tracks is not None:
        album['tracks'] = tracks

    return album

# print(make_album('Kendrick Lamar', 'Section.80'))
# print(make_album('MGMT', 'Time to Pretend', 5))

while True:
    artist = input("Please enter the artist's name: ")
    if artist == 'q':
        break

    title = input("PLease enter the album title: ")
    if title == 'q':
        break

    print(make_album(artist, title))
