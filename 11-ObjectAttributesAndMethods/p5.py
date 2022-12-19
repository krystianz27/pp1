class Artist():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (f"Performer: {self.artist} \nSong: {self.title} \nAlbum: {self.album} \nYear: {self.year}")



my_artist1 = Artist("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
print(my_artist1)
print()

my_artist2 = Artist("Artist2", "Title2", "Album2", "2022")
print(my_artist2)


